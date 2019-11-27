from django.shortcuts import render

# Create your views here.
def add_post(request, template_name= "feed/add_post.html"):
    return render(request, template_name)

def delete_post(request, template_name= "feed/delete_post.html"):
    return render(request, template_name)

def view_post(request, template_name= "feed/view_post.html"):
    return render(request, template_name)

def view_feed(request, template_name= "feed/view_feed.html"):
    return render(request, template_name)