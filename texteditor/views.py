from django.shortcuts import render
from .forms import MarkdownForm

# Create your views here.
def render_markdown_editor_template( request, template_name="texteditor/markdown_text_editor.html"):
	""" Renders the text editor template for markdown view"""
	markdownform = MarkdownForm()
	template_render_data = {'markdownform':markdownform}
	return render(request, template_name, template_render_data)
