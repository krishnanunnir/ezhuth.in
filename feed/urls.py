from django.urls import path
from feed import views

app_name = 'feed'
urlpatterns = [
    path('all/', views.view_all, name= 'view_all'),
    path('feed/', views.view_feed, name= 'view_feed'),
    path('add/', views.add_post, name= 'add_post'),
    path('view/<int:post_id>/', views.view_post, name= 'view_post'),
    path('edit/<int:post_id>', views.edit_post, name= 'edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name= 'delete_post'),
    path('drafts/',views.view_drafts, name= 'view_drafts'),
]