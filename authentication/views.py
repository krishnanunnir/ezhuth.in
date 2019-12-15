from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
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
            messages.warning(request, 'Invalid username or password')
    loginform = LoginForm()
    template_data = {'loginform': loginform}
    return render(request, template_name, template_data)

def render_signup_page(request, template_name= "authentication/signup_page.html"):
    if request.user.is_authenticated:
        return HttpResponseRedirect(login_success)
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(data= request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(signup_success)
    #case for error occurence or get request to the page
    template_data = {'form': form}
    return render(request, template_name, template_data)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(logout_success)

@login_required
def render_user_profile(request, template_name= "authentication/user_profile.html"):
    currentuser = request.user
    template_data = {'currentuser': currentuser}
    return render(request, template_name, template_data)