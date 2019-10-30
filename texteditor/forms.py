from django import forms

class MarkdownForm(forms.Form):
    post_title = forms.CharField(label='title', max_length=256, widget=forms.TextInput(attrs={'autocomplete':'off','id':'post_title_id','placeholder':'Post Title','class':'form-control'}))
    post_content = forms.CharField(widget=forms.Textarea(attrs={'autocomplete':'off','id':'post_content_id','placeholder':'Post Content','class':'form-control'}))
    post_author = forms.CharField(label='Author', max_length=256, widget=forms.TextInput(attrs={'autocomplete':'off','id':'post_author_id','placeholder':'Post Author','class':'form-control'}))
