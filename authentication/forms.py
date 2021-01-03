# Create your forms here.
from django import forms
from allauth.account.forms import SignupForm

class UserSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',required=True,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
 
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user