from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import AddPostForm

# Create your views here.
@login_required
def add_post(request, template_name= "feed/add_post.html"):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Post(title= title, content= content, author= user).save()
        return HttpResponse('Value added successfully')
    else:
        addpostform = AddPostForm()
        template_data = {'addpostform':addpostform}
        return render(request, template_name, template_data)

@login_required
def delete_post(request, post_id, template_name= "feed/delete_post.html"):
    Post.objects.get(id= post_id).delete()
    return HttpResponse("The value has been deleted successfully")

@login_required
def view_post(request, post_id, template_name= "feed/view_post.html"):
    post = Post.objects.get(id = post_id)
    template_data = {'post': post}
    return render(request, template_name, template_data)

@login_required
def view_feed(request, template_name= "feed/view_feed.html"):
    allposts = Post.objects.all()
    template_data = {'allposts': allposts}
    return render(request, template_name, template_data)