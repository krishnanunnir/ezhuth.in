from django.http.response import HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Q
from django.db.models import Count
from django.http import JsonResponse

from .models import Post, Comment, Like
from .forms import AddPostForm, AddCommentForm, ImageUploadForm
from .redirects import *
from .utils import is_ajax, paginate_posts


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
            # save post in feed or draft depending on the button present in request.POST
            if 'publish' in request.POST:
                status = 1
                # messages.info(request, 'New Post added successfully')
                # setting redirect_url to feed page or draft page
                redirect_url = feed_home
            else:
                status = 0
                # messages.info(request, 'New Draft added successfully')
                redirect_url = drafts_home
            post = Post.objects.create(title= title, content= content, author= request.user, status= status)
            liked_object = Like.objects.create(content_object=post)
            liked_object.users.add(request.user)
            return HttpResponseRedirect(redirect_url)
    template_data = {'form':form}
    return render(request, template_name, template_data)


@login_required
def edit_post(request, post_slug, template_name= "feed/add_post.html"):
    """ Edit already saved posts or drafts """
    post = get_object_or_404(Post, slug= post_slug, author= request.user)
    if request.method == 'POST':
        #Sanitizing data using AddPostForm since both of them use the same data
        form = AddPostForm(request.POST)
        if form.is_valid():           
            post.title = form.cleaned_data.get('title')
            post.content = form.cleaned_data.get('content')
            if 'publish' in request.POST:
                post.status = 1
                # messages.info(request, 'Post added to feed')
                redirect_url = feed_home
            else:
                post.status = 0
                # messages.info(request, 'Post updated in Drafts')
                redirect_url = drafts_home
            post.save()
            return HttpResponseRedirect(redirect_url)
    form = AddPostForm(initial= {'title':post.title, 'content':post.content})
    template_data = {'form': form}
    return render(request, template_name, template_data)



def view_post(request, post_slug, template_name= "feed/view_post.html"):
    # Makes a post visible if you are the owner or if the post status is set to published
    display_comment_form = False
    try:
        post = get_object_or_404(Post, Q(slug= post_slug) & (Q(author= request.user) | Q(status= 1)))
        if post.comments_enabled:
            display_comment_form = True
    except TypeError:
        # Condition of trying to access a post while not logged in
        # Comments are turned off since only logged in user can comment
        post = get_object_or_404(Post, Q(slug= post_slug) & Q(status= 1))
    comments = post.comment
    form = AddCommentForm()
    # Comments can only be added if the post is published
    display_comment_form = display_comment_form and (post.status==1)
    if request.method=="POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            # messages.info(request, 'Comment added for '+post.title)
            title = "Replied to '%s'" %(post.title)
            comment = Comment.objects.create(content_object=post, content= content, author= request.user)
            liked_object = Like.objects.create(content_object=comment)
            liked_object.users.add(request.user)
            return HttpResponseRedirect('/view/' + str(post_slug))
    # Options for modifying post is only visible to the author of the post
    modify_status = post.author==request.user
    template_data = {'post': post,'modify_status': modify_status,'comments':comments,'form':form,'display_comment_form':display_comment_form}
    return render(request, template_name, template_data)


@login_required
def delete_post(request, post_slug):
    """ Delete a post given the post_id """
    post = get_object_or_404(Post, slug= post_slug, author= request.user)
    post_status = post.status
    post.delete()
    # A different message is displayed if it is post or Draft and set redirect url
    if post_status == 0:
        # messages.info(request, 'Draft deleted successfully')
        redirect_url = drafts_home
    else:
        # messages.info(request, 'Post deleted successfully')
        redirect_url = feed_home
    return HttpResponseRedirect(redirect_url)

@require_GET
def view_all(request, template_name= "feed/view_posts.html"):
    """ Print all the publicly visible posts """
    all_posts = Post.objects.annotate(num_val=(Count('comment'))).order_by('-num_val')
    # time_threshold = datetime.now() - timedelta(hours=24)
    all_posts = all_posts.filter(status=1)
    posts = paginate_posts(request, all_posts, 10)
    template_data = {'posts': posts}
    if is_ajax(request):
        return render(request, 'feed/__posts.html', template_data)
    return render(request, template_name, template_data)


@login_required
@require_GET
def view_feed(request, template_name= "feed/view_posts.html"):
    """ Print the users feed """
    all_posts = Post.objects.filter(status= 1, author= request.user)
    posts = paginate_posts(request, all_posts, 10)
    template_data = {'posts': posts,'show_selected_user': True} 
    if is_ajax(request):
        return render(request, 'feed/__posts.html', template_data)
    return render(request, template_name, template_data)

@require_GET
@login_required
def view_drafts(request, template_name= "feed/view_posts.html"):
    """ Renders all drafts """
    all_posts = Post.objects.filter(status= 0, author= request.user)
    posts = paginate_posts(request, all_posts, 10)
    template_data = {'posts': posts}
    if is_ajax(request):
        return render(request, 'feed/__posts.html', template_data)
    return render(request, template_name, template_data)

def view_user(request, username, template_name= "feed/view_posts.html"):
    """ Print the users feed """
    user = get_object_or_404(User, username= username)
    all_posts = Post.objects.filter(status= 1, author= user)
    posts = paginate_posts(request, all_posts, 10)
    template_data = {'posts': posts,'selected_user': user, 'show_selected_user': True} 
    if is_ajax(request):
        return render(request, 'feed/__posts.html', template_data)
    return render(request, template_name, template_data)

@login_required
def like_post(request, post_slug):
    if is_ajax(request):
        post = get_object_or_404(Post, slug= post_slug, status=1)
        liked_object = Like.objects.get(like_for_post=post)
        if request.user in liked_object.users.all():
            liked_object.users.remove(request.user)
            return HttpResponse("false")
        else:
            liked_object.users.add(request.user)
            return HttpResponse("true")
    else:
        raise Http404("Page not found")

@login_required
def like_comment(request, id):
    if is_ajax(request):
        comment = get_object_or_404(Comment, id= id)
        liked_object = Like.objects.get(like_for_comment=comment)
        if request.user in liked_object.users.all():
            liked_object.users.remove(request.user)
            return HttpResponse("false")
        else:
            liked_object.users.add(request.user)
            return HttpResponse("true")
    else:
        raise Http404("Page not found")

@login_required
@require_POST
def handle_image(request):
    form = ImageUploadForm()
    if request.method=="POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            responseData = {
                'location': item.image.url
            }
            return JsonResponse(responseData)
    return HttpResponseServerError()