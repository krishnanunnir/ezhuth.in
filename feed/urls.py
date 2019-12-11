from django.urls import path
from feed import views

app_name = 'feed'
urlpatterns = [
    path('feed/', views.view_feed, name= 'view_feed'),
    path('feed/add/', views.add_post, name= 'add_post'),
    path('feed/delete/<int:post_id>/', views.delete_post, name= 'delete_post'),
    path('feed/view/<int:post_id>/', views.view_post, name= 'view_post'),
    path('drafts/',views.view_drafts, name= 'view_drafts'),
    path('drafts/editdraft/<int:post_id>',views.edit_draft, name= 'edit_draft')
]