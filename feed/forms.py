from django import forms
from .models import ImageTinymce, Post, Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ടൈറ്റിൽ'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageTinymce
        fields =('image',)