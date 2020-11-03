from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ടൈറ്റിൽ'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)