from django.shortcuts import render

# Create your views here.
def render_markdown_editor_template(request,template_name="texteditor/markdown_text_editor.html"):
	""" Renders the text editor template for markdown view"""
	return render(request, template_name)
