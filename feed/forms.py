from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description', 'content')
        widgets = {
            'content': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'placeholder': 'തലക്കെട്ടെ'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'