from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.models import User
from regForms import RegistrationForm

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register(request):
	form = RegistrationForm()
	templ_name=''
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user( ### need to query if the name existed ?.
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
			)
			return HttpResponseRedirect('/register/success/')
		else:
			templ_name = 'registration/register.html'
	variables = RequestContext(request, { 'form':form} )
	return render_to_response(templ_name,variables)
