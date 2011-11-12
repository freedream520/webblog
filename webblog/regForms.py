#coding=utf8
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
	username = forms.CharField(label='username',max_length=30)
	email = forms.EmailField(label='Email',required=False)
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
	password2 = forms.CharField(label='Password(Again)',widget=forms.PasswordInput())

	def cleaned_password2(self):
		if 'password1' in self.cleaned_data:
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2 :
				return password2
		raise forms.ValidationError('两次输入密码不一致 Passwords do not match')
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$',username):
			raise forms.ValidationError('名字只能由字母和下划线组成 Username can only conatain alphanumeric characters and the undersocre.')
		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('用户名已存在 Username is already existed.')
