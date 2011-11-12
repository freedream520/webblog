from codeShare.models import Snippet,Language
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext

# Create your views here.

def show_all(request):
	obj_list = Snippet.objects.all()
	variables = RequestContext(request,{'obj_list':obj_list})
	return render_to_response('snippet/show_all.html',variables)

def show_snippet_by_id(request,sp_id):
	obj = []
	obj = Snippet.objects.get(id=sp_id)
	variables = RequestContext(request,{'obj':obj})
	return render_to_response('snippet/show_detail.html',variables)
	
def show_by_lang(request,lang_id):
	obj_list = Snippet.objects.all().filter(language__id=lang_id)
	variables = RequestContext(request,{'obj_list':obj_list,'lang_name':obj_list[0].language})
	return render_to_response('snippet/show_all.html',variables)
