from django.urls import path
from feed import views

app_name = 'feed'
urlpatterns = [
    path('feed/', views.view_feed, name= 'view_feed'),
    path('feed/add/', views.add_post, name= 'add_post'),
    path('feed/delete/<int:post_id>/', views.delete, name= 'delete_post'),
    path('feed/edit/<int:post_id>', views.edit, name= 'edit_post'),
    path('feed/view/<int:post_id>/', views.view, name= 'view_post'),
    path('drafts/',views.view_drafts, name= 'view_drafts'),
    path('drafts/edit/<int:post_id>', views.edit, name= 'edit_draft'),
    path('drafts/delete/<int:post_id>', views.delete, name= 'delete_draft'),
    path('drafts/view/<int:post_id>/', views.view, name= 'view_draft'),
]