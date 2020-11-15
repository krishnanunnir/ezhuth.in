from django import forms
from .models import ImageTinymce, Post, Comment
from django.utils.translation import ugettext_lazy as _
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ടൈറ്റിൽ'}),
        }
        labels = {
            "content": _("Post")
        }
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'The {fieldname} is empty.'.format(
                fieldname=field.label)}

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            "content": _("Comment")
        }
    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is empty'.format(
                fieldname=field.label)}

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageTinymce
        fields =('image',)