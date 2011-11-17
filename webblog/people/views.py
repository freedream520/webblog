# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from people.models import *
from people.forms import FriendInviteForm

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

@login_required()
def show_friend(request):
	obj_list = []
	user = request.user
	try:
		obj_list = FriendShip.objects.all()
		obj_list = obj_list.filter(from_friend__exact = user )
	except:
		pass
	varialbles = RequestContext(request, {'obj_list':obj_list} )
	return render_to_response('people/show_friend.html',varialbles)




@login_required 
def confirm_friendship(request,f_id):
	u_id = request.user
	obj = FriendShip.get(from_friend=f_id,to_friend=u_id)
	obj.status = True
	obj.save()
	try:
		newShip = FriendShip(from_friend=u_id , to_friend=f_id,status = True)
		newShip.save()
	except:
		pass
	varialbles = RequestContext(request, {'msg':"%s , %s are now firends :) " % (u_id.username,f_id.username)})
	return render_to_response('people/friend_msg.html',varialbles)

@login_required
def ignore_msg(request,msg_id):
	# f_id stands for the Msg's id , that the people want to delete.
	msg = Msg.objects.get(id = msg_id,to_user = request.user.id )
	msg.delete()
	return HttpResponseRedirect( '/people/%d/' % request.user.id )
	
	
@login_required 
def delete_friendship(request,f_id):
	varialbles = RequestContext(request,{})
	return render_to_response('',varialbles)

@login_required
def friend_invite(request):
	#derrors = []
	if request.method == 'POST':
		form = FriendInviteForm(request.POST)
		if form.is_valid():
			invitation = Invitation(
				name = form.cleaned_data['name'],
				email = form.cleaned_data['email'],
				code = User.objects.make_random_password(20),
				sender = request.user,
				receiver = User.objects.get(id=request.POST['recv_id'])
			)
			invitation.save()
			invitation.send()
			return HttpResponseRedirect( request.POST['next'] )
		else:
			form = FriendInviteForm()
		varialbles = RequestContext(request,{'form':form})
		return render_to_response('people/invite.html',varialbles)

@login_required
def friend_accept(request,ac_code):
	try:
		invitation = Invitation.objects.get(code__exact=ac_code)
		request.session['invitation'] = invitation.id
	except:
		pass
	return HttpResponseRedirect('/make/friend/')

@login_required
def make_friend(request):
	if 'invitation' in request.session:
		invitation = Invitation.objects.get(id = request.session['invitation'] )
		friendship = FriendShip(from_friend=request.user,to_friend=invitation.sender)
		friendship.save()
		friendship = FriendShip(from_friend=invitation.sender,to_friend=request.user)
		friendship.save()
		msg = Msg.objects.get(from_user = invitation.sender , to_user=request.user ,msg_type=3)
		msg.delete()
		invitation.delete()
		del request.session['invitation']
		return HttpResponseRedirect('/friends/')
	else:
		return HttpResponseRedirect('/')

#def register_confirm(request,ac_code):
#	try:
#		User.objects.get(code__exact
#	
	
	
