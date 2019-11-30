from django.shortcuts import render
from django.http import Http404
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
        status = 0
        if 'publish' in request.POST:
            status = 1
        Post(title= title, content= content, author= user, status= status).save()
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
    publishedposts = Post.objects.filter(status= 1)
    template_data = {'publishedposts': publishedposts}
    return render(request, template_name, template_data)

def view_drafts(request, template_name= "feed/view_drafts.html"):
    draftposts = Post.objects.filter(status= 0)
    template_data = {'draftposts': draftposts}
    return render(request, template_name, template_data)

def edit_draft(request, post_id, template_name= "feed/edit_draft.html"):
    if request.method == 'POST':
        editpost = Post.objects.get(id= post_id)
        if(editpost.author != request.user):
            raise Http404
        editpost.title = request.POST.get('title')
        editpost.content = request.POST.get('content')
        editpost.status = 0
        if 'publish' in request.POST:
            editpost.status = 1
        editpost.save()
        return HttpResponse('Value added successfully')
    else:
        draft_post = Post.objects.get(id= post_id);
        editdraftpost= AddPostForm(initial= {'title':draft_post.title, 'content':draft_post.content })
        template_data = {'editdraftpost': editdraftpost}
        return render(request, template_name, template_data)
