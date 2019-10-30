from django.shortcuts import render

# Create your views here.
def render_markdown_editor_template( request, template_name="texteditor/markdown_text_editor.html", page_title="Texteditor", base_template="base.html"):
	""" Renders the text editor template for markdown view"""
	template_render_data = {'page_title': page_title,'base_template': base_template}
	return render(request, template_name, template_render_data)
