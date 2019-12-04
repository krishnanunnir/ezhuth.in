from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from .models import Post
from .forms import AddPostForm

# Create your views here.
@login_required
def add_post(request, template_name= "feed/add_post.html"):
    if request.method == 'POST':
        addpostform = AddPostForm(request.POST)
        if addpostform.is_valid():
            title = addpostform.cleaned_data.get('title')
            content = addpostform.cleaned_data.get('content')
            user = request.user
            if 'publish' in request.POST:
                status = 1
            else:
                status = 0
            Post(title= title, content= content, author= user, status= status).save()
            return HttpResponse('Value added successfully')
        else:
            return HttpResponse('There was an error with the program')
    else:
        addpostform = AddPostForm()
        template_data = {'addpostform':addpostform}
        return render(request, template_name, template_data)

@login_required
def delete_post(request, post_id, template_name= "feed/delete_post.html"):
    get_object_or_404(Post, id= post_id, author= request.user, status= 1).delete()
    return HttpResponse("The value has been deleted successfully")

@login_required
def view_post(request, post_id, template_name= "feed/view_post.html"):
    post = get_object_or_404(Post, id= post_id, author= request.user, status= 1)
    template_data = {'post': post}
    return render(request, template_name, template_data)

@login_required
def view_feed(request, template_name= "feed/view_feed.html"):
    publishedposts = Post.objects.filter(status= 1, author= request.user)
    if not publishedposts.exists():
        raise Http404("Sorry, this page doesn't exist")
    template_data = {'publishedposts': publishedposts}
    return render(request, template_name, template_data)

@login_required
def view_drafts(request, template_name= "feed/view_drafts.html"):
    draftposts = Post.objects.filter(status= 0, author= request.user)
    if not draftposts.exists():
        raise Http404("Sorry, this page doesn't exist")
    template_data = {'draftposts': draftposts}
    return render(request, template_name, template_data)
@login_required
def edit_draft(request, post_id, template_name= "feed/edit_draft.html"):
    if request.method == 'POST':
        editpost = get_object_or_404(Post, id= post_id, author= request.user, status= 0)
        editpostform = AddPostForm(request.POST) #Sanitizing data using AddPostForm since both of them use the same data
        if editpostform.is_valid():           
            editpost.title = editpostform.cleaned_data.get('title')
            editpost.content = editpostform.cleaned_data.get('content')
            if 'publish' in request.POST:
                editpost.status = 1
            else:
                editpost.status = 0
            editpost.save()
            return HttpResponse('Value added successfully')
        else:
            print(editpostform.errors)
            return HttpResponse("There was an error with the data")
    else:
        draftpost = get_object_or_404(Post, id= post_id, author= request.user, status= 0)
        editdraftpost= AddPostForm(initial= {'title':draftpost.title, 'content':draftpost.content })
        template_data = {'editdraftpost': editdraftpost}
        return render(request, template_name, template_data)
