from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, LoginForm
from .redirects import *

def render_login_page(request, template_name= "authentication/login_page.html"):
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_success)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password= password)
        if user:
            login(request, user)
            return HttpResponseRedirect(login_success)
        else:
            return HttpResponse("sorry, no such user")
    else:
        loginform = LoginForm()
        template_data = {'loginform': loginform}
        return render(request, template_name, template_data)

def render_signup_page(request, template_name= "authentication/signup_page.html"):
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_success)
    if request.method == "POST":
        signupform = SignupForm(data= request.POST)
        if signupform.is_valid():
            user = signupform.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse("user signed up")
    else:
        signupform = SignupForm()
        template_data = {'signupform': signupform}
        return render(request, template_name, template_data)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("User logged out")

@login_required
def render_user_profile(request, template_name= "authentication/user_profile.html"):
    currentuser = request.user
    template_data = {'currentuser': currentuser}
    return render(request, template_name, template_data)