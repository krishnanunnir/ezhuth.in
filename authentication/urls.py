from django.urls import path
from authentication import views

app_name = 'authentication'
urlpatterns = [
    path('login/', views.render_login_page, name= 'render_login_page'),
    path('signup/', views.render_signup_page, name= 'render_signup_page'),
    path('profile/', views.render_user_profile, name= 'render_user_profile'),
    path('logout/', views.logout_user, name= "logout_user"),
]