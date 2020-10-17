from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description', 'content')
        widgets = {
            'content': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'placeholder': 'ടൈറ്റിൽ'}),
            'description': forms.TextInput(attrs={'placeholder': 'ഡിസ്ക്രിപ്ഷൻ '}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)