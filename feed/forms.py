from django import forms
from .models import ImageTinymce, Post, Comment
from django.utils.translation import ugettext as _
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.Textarea(attrs={'placeholder': _('Title'), 'height':'5em'}),
            'content': forms.HiddenInput(),
        }
        labels = {
            "content": _("Post")
        }
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':_('The {fieldname} is empty.').format(
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
            field.error_messages = {'required':_('{fieldname} is empty').format(
                fieldname=field.label)}

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageTinymce
        fields =('image',)

class PreviewForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('header_image','description')
        widgets = {
            'header_image': forms.FileInput()
        }