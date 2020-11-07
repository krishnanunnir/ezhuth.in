from django import forms
from .models import ImageTinymce, Post, Comment

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ടൈറ്റിൽ'}),
        }
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label)}

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageTinymce
        fields =('image',)