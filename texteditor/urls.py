from django.urls import path
from texteditor import views

urlpatterns = [
    path('', views.render_markdown_editor_template, name='render_markdown_editor_template'),
]