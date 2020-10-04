from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {'content': forms.HiddenInput()}
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # Adding bootstrap class form-control to all fields
            visible.field.widget.attrs['class'] = 'form-control'

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'