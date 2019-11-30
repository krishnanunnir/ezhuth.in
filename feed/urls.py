from django.urls import path
from feed import views

app_name = 'feed'
urlpatterns = [
    path('', views.view_feed, name= 'view_feed'),
    path('add/', views.add_post, name= 'add_post'),
    path('delete/<int:post_id>/', views.delete_post, name= 'delete_post'),
    path('view/<int:post_id>/', views.view_post, name= 'view_post'),
    path('drafts/',views.view_drafts, name= 'view_drafts'),
    path('editdraft/<int:post_id>',views.edit_draft, name= 'edit_draft')
]