#coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
import datetime
# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=100)
	parent = models.ForeignKey('self',blank=True,null=True)
	level = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class Photo(models.Model):
	active = models.BooleanField(default=True)
	owner = models.ForeignKey(User)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to='images/headshot')	
	
	# for thumbnail to set a physic path for the headshots

	def get_img_url(self):
		return "%s" % self.image.url
	
	def __unicode__(self):
		return '%s\' images' % self.owner.username
		
class People(models.Model):
	GENDER_CHOICES = (
    	(1,u'Male男'),
		(0,u'Female女'),
		)
	name = models.ForeignKey(User)
	depart = models.ForeignKey(Department)
	headshot = models.ForeignKey(Photo)
	sex = models.IntegerField(choices=GENDER_CHOICES)#0 women; 1 men
	birthday = models.DateTimeField()#should before today and less than 150?
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.name.username
	
class Msg(models.Model):
	MSG_TYPES = (
		(1,u'system'),
		(2,u'user'),
		(3,u'friend'),
	)
	title = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	from_user = models.ForeignKey(User,related_name='from_u')
	to_user = models.ForeignKey(User,related_name='to_u')
	pub_date = models.DateTimeField(default = datetime.datetime.now() )
	bool_read = models.BooleanField(default=False)
	parent = models.ForeignKey('self',blank=True,null=True)
	msg_type = models.IntegerField(choices = MSG_TYPES)

	def __unicode__(self):
		return self.title


class FriendShip(models.Model):
	from_friend = models.ForeignKey(User,related_name='friend_set')
	to_friend = models.ForeignKey(User,related_name='to_firend_set',blank=True)

	def __unicode__(self):
		return "friendship from %s to %s "  % (self.from_friend.username,self.to_friend.username)
	
	class Meta:
		unique_together = (('to_friend','from_friend'),)
	
class Invitation(models.Model):
	# send a link to invite a friendship.
	name = models.CharField(max_length=50)
	email = models.EmailField()
	code = models.CharField(max_length=20)
	sender = models.ForeignKey(User)
	receiver = models.ForeignKey(User,related_name='receiver_name')

	def __unicode__(self):
		return "%s send a email to this address(name is %s):%s" % ( self.sender.username, self.name , self.email)
	
	def send(self):
		subject = 'invitation to join my django site.(by fever)'
		link = 'http://%s/friend/accept/%s/' % (settings.SITE_HOST , self.code)
		# send link via the system's message
		msg = Msg(title='add friend apply ',content = link, from_user = self.sender , to_user = self.receiver , msg_type = 3 )
		msg.save()
		### send the link via email
		template = get_template('invite_email.txt')
		context = Context({
			'name':self.name,
			'link':link,
			'sender':self.sender.username,
		})
		message = template.render(context)
		# send the mail ,  just umcomment this below.
		#send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[self.email])

