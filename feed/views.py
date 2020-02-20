from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Post
from .forms import AddPostForm
from .redirects import *

# Create your views here.
@login_required
def add_post(request, template_name= "feed/add_post.html"):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            description = form.cleaned_data.get('description')
            user = request.user
            if 'publish' in request.POST:
                status = 1
                messages.info(request, 'New Post added successfully')
                redirect_url = feed_home
            else:
                status = 0
                messages.info(request, 'New Draft added successfully')
                redirect_url = drafts_home
            Post(title= title, content= content, description= description, author= user, status= status).save()
            return HttpResponseRedirect(redirect_url)
    template_data = {'form':form}
    return render(request, template_name, template_data)


@login_required
def edit_post(request, post_id, template_name= "feed/edit_post.html"):
    post = get_object_or_404(Post, id= post_id, author= request.user)
    if request.method == 'POST':
        form = AddPostForm(request.POST) #Sanitizing data using AddPostForm since both of them use the same data
        if form.is_valid():           
            post.title = form.cleaned_data.get('title')
            post.content = form.cleaned_data.get('content')
            post.description = form.cleaned_data.get('description')
            if 'publish' in request.POST:
                post.status = 1
                messages.info(request, 'Post added to feed')
                redirect_url = feed_home
            else:
                post.status = 0
                messages.info(request, 'Post updated in Drafts')
                redirect_url = drafts_home
            post.save()
            return HttpResponseRedirect(redirect_url)
    form = AddPostForm(initial= {'title':post.title, 'content':post.content, 'description':post.description })
    template_data = {'form': form}
    return render(request, template_name, template_data)


@login_required
def view_post(request, post_id, template_name= "feed/view_post.html"):
    post = get_object_or_404(Post, Q(id= post_id), Q(author= request.user) | Q(status= 1)) # Makes a post visible if you are the owner or if the post status is set to published
    modify_status = post.author==request.user
    template_data = {'post': post,'modify_status': modify_status}
    return render(request, template_name, template_data)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id= post_id, author= request.user)
    post_status = post.status
    post.delete()
    if post_status == 0:
        messages.info(request, 'Draft deleted successfully')
        redirect_url = drafts_home
    else:
        messages.info(request, 'Post deleted successfully')
        redirect_url = feed_home
    return HttpResponseRedirect(redirect_url)


def view_all(request, template_name= "feed/view_posts.html"):
    """ Print all the publicly visible posts """
    posts = Post.objects.filter(status= 1)
    if not posts.exists():
        messages.info(request, "No content to display")
    template_data = {'posts': posts}
    return render(request, template_name, template_data)


@login_required
def view_feed(request, template_name= "feed/view_posts.html"):
    """ Print the users feed """
    posts = Post.objects.filter(status= 1, author= request.user)
    if not posts.exists():
        messages.info(request, "No content to display")
    template_data = {'posts': posts}
    return render(request, template_name, template_data)

@login_required
def view_drafts(request, template_name= "feed/view_posts.html"):
    posts = Post.objects.filter(status= 0, author= request.user)
    if not posts.exists():
        messages.info(request, "No content to display")
    template_data = {'posts': posts}
    return render(request, template_name, template_data)