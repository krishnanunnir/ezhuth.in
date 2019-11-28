from django.urls import path
from feed import views

app_name = 'feed'
urlpatterns = [
    path('add/', views.add_post, name= 'add_post'),
    path('delete/<int:post_id>/', views.delete_post, name= 'delete_post'),
    path('view/<int:post_id>/', views.view_post, name= 'view_post'),
    path('', views.view_feed, name= 'view_feed'),
]