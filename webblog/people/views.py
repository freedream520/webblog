# Create your views here.
from people.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required()
def show_people_by_id(request,p_id):
	obj = []
	user = request.user
	if user:
		obj = People.objects.get(name=p_id)
	varialbles = RequestContext(request,{'obj':obj,'user':user})
	return render_to_response('people/show_p_by_id.html',varialbles)


@login_required()
def show_all_people(request):
	obj = People.objects.all()
	varialbles = RequestContext(request,{'object_list':obj})
	return render_to_response('people/people_archive.html',varialbles)


