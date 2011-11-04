from codeShare.models import Snippet
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext

# Create your views here.

def show_all(request):
	obj_list = Snippet.objects.all()
	variables = RequestContext(request,{'obj_list':obj_list})
	return render_to_response('snippet/show_all.html',variables)
