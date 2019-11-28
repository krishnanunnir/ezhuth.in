from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddPostForm
from .models import Post

# Create your views here.
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

def delete_post(request, template_name= "feed/delete_post.html"):
    return render(request, template_name)

def view_post(request, template_name= "feed/view_post.html"):
    return render(request, template_name)

def view_feed(request, template_name= "feed/view_feed.html"):
    return render(request, template_name)