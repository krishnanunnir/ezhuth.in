from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    fields = ('username','password')

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta():
        model = User
        fields = ('username', 'password', 'confirm_password','email')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Define an error if password and confirm password are not the same
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )