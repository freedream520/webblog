# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from people.models import *

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


@login_required()
def show_msg_by_id(request,msg_id):
	msg = []
	user = request.user
	try:
		msg = Msg.objects.get(id=msg_id,to_user=user)
		msg.bool_read = True
		msg.save()
	except:
		pass
	varialbles = RequestContext(request,{'msg':msg})
	return render_to_response('people/show_msg_by_id.html',varialbles)
