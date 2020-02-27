from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Post,Comment
from .forms import AddPostForm,AddCommentForm
from .redirects import *

# Create your views here.
@login_required
def add_post(request, template_name= "feed/add_post.html"):
    """ For adding posts and drafts"""
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            description = form.cleaned_data.get('description')
            user = request.user
            # save post in feed or draft depending on the button present in request.POST
            if 'publish' in request.POST:
                status = 1
                messages.info(request, 'New Post added successfully')
                # setting redirect_url to feed page or draft page
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
    """ Edit already saved posts or drafts """
    post = get_object_or_404(Post, id= post_id, author= request.user)
    if request.method == 'POST':
        #Sanitizing data using AddPostForm since both of them use the same data
        form = AddPostForm(request.POST)
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
    comments = Comment.objects.filter(post= post_id)
    form = AddCommentForm()
    # Makes a post visible if you are the owner or if the post status is set to published
    post = get_object_or_404(Post, Q(id= post_id), Q(author= request.user) | Q(status= 1))
    # Comments can only be added if the post is published
    display_comment_form = post.status==1
    if request.method=="POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            messages.info(request, 'Comment added for '+post.title)
            Comment(author= request.user,content= content,post= post).save()
            return HttpResponseRedirect('/view/' + str(post_id))
    # Options for modifying post is only visible to the author of the post
    modify_status = post.author==request.user
    template_data = {'post': post,'modify_status': modify_status,'comments':comments,'form':form,'display_comment_form':display_comment_form}
    return render(request, template_name, template_data)


@login_required
def delete_post(request, post_id):
    """ Delete a post given the post_id """
    post = get_object_or_404(Post, id= post_id, author= request.user)
    post_status = post.status
    post.delete()
    # A different message is displayed if it is post or Draft and set redirect url
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
    """ Renders all drafts """
    posts = Post.objects.filter(status= 0, author= request.user)
    if not posts.exists():
        messages.info(request, "No content to display")
    template_data = {'posts': posts}
    return render(request, template_name, template_data)

@login_required
def render_comment( request, post_id, template_name= "feed/comments.html"):
    """ Renders the comments for a post given the post_id"""
    comments = Comment.objects.filter(post= post_id)
    form = AddCommentForm()
    post =  get_object_or_404(Post, id= post_id, status= 1)
    if request.method=="POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            messages.info(request, 'Comment added for')
            Comment(author= request.user,content= content,post= post).save()
            return HttpResponseRedirect('/view/' + str(post_id))
    template_data = {'comments': comments, 'form': form}
    return render(request,template_name,template_data)