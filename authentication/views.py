from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import SignupForm, LoginForm
from .redirects import *

def render_login_page(request, template_name= "authentication/login_page.html"):
    """ Renders the login page and processes signup requests """
    # If user is already logged in then redirect to another html
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_success)
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email= email, password= password)
            if user:
                login(request, user)
                return HttpResponseRedirect(login_success)
            else:
                messages.success(request, 'Invalid email or password')
    template_data = {'form': form}
    return render(request, template_name, template_data)

def render_signup_page(request, template_name= "authentication/signup_page.html"):
    """ Render signup page signup requests"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_success)
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(data= request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                validate_password(user.password, user)
                user.set_password(user.password)
                user.save()
                messages.info(request, 'Account created successfully!')
                return HttpResponseRedirect(signup_success)
            except ValidationError as e:
                form.add_error('password', e)  # to be displayed with the field's errors
    # case for error occurence or get request to the page
    template_data = {'form': form}
    return render(request, template_name, template_data)

@login_required
def logout_user(request):
    """ User requests logout """
    messages.success(request, 'Logged out successfully')
    logout(request)
    return HttpResponseRedirect(logout_success)

@login_required
def render_user_profile(request, template_name= "authentication/user_profile.html"):
    """ Renders user profile """
    currentuser = request.user
    template_data = {'currentuser': currentuser}
    return render(request, template_name, template_data)