from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description', 'content')
        widgets = {
            'content': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description '}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)