from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class LoginForm(forms.Form):
    password = forms.CharField(label="password",widget=forms.PasswordInput( attrs={'placeholder': 'Password'}))
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(fieldname=field.label)}

class SignupForm(forms.ModelForm):
    confirm_password=forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta():
        model = User
        fields = ('username', 'password', 'confirm_password','email')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
            'confirm_password': PasswordInput(attrs={'placeholder': 'Confirm Password'}),
            'email': EmailInput(attrs={'placeholder':'Email'})
        }
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(fieldname=field.label)}

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Define an error if password and confirm password are not the same
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
