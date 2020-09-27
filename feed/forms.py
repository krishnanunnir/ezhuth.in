from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class AddPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ('title', 'content')
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