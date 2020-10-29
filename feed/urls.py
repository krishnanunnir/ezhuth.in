from django.urls import path, register_converter
from feed import views
from . import converters

register_converter(converters.UsernameConverter, 'username')

app_name = 'feed'
urlpatterns = [
    path('', views.view_all, name= 'view_all'),
    path('feed/', views.view_feed, name= 'view_feed'),
    path('add/', views.add_post, name= 'add_post'),
    path('view/<slug:post_slug>', views.view_post, name= 'view_post'),
    path('edit/<slug:post_slug>', views.edit_post, name= 'edit_post'),
    path('user/<username:username>', views.view_user, name= 'view_user'),
    path('delete/<slug:post_slug>', views.delete_post, name= 'delete_post'),
]