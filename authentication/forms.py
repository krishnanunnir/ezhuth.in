from django import forms
from .models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class LoginForm(forms.Form):
    password = forms.CharField(label="password",widget=PasswordInput( attrs={'placeholder': 'Password'}))
    email = forms.EmailField(label="email",widget= EmailInput(attrs={'placeholder':'Email'}))
    fields = ('email','password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(fieldname=field.label)}

class SignupForm(forms.ModelForm):
    confirm_password=forms.CharField(label="confirm password", required= True, widget= PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(label="first name", required= True, widget= TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label="last name", required= True, widget = TextInput(attrs={'placeholder': 'Last Name'}))
    class Meta():
        model = User
        fields = ('first_name','last_name','email','password', 'confirm_password')
        widgets = {
            'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
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
