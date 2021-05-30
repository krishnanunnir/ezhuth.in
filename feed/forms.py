from django import forms
from django.utils.translation import ugettext as _

from .models import Comment, ImageTinymce, Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        widgets = {
            "title": forms.HiddenInput(),
            "content": forms.HiddenInput(),
        }
        labels = {"content": _("Post")}

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(AddPostForm, self)
        if self.cleaned_data["content"] == "" or self.cleaned_data["title"] == None:
            raise forms.ValidationError("Please add post title and content.")


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        widgets = {
            "title": forms.HiddenInput(),
            "content": forms.HiddenInput(),
        }
        labels = {"content": _("Post")}

    def __init__(self, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {"content": _("Comment")}

    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {
                "required": _("{fieldname} is empty").format(fieldname=field.label)
            }


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageTinymce
        fields = ("image",)


class PreviewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("header_image", "description")
        widgets = {"header_image": forms.FileInput()}
