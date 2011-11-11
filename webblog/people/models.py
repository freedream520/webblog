#coding=utf8
from django.db import models
from django.contrib.auth.models import User
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
	
	def get_img_url(self):
		return "%s" % self.image.url
	
	def save(self):
		temp = Photo.objects.all().filter(active=True,owner__id=self.owner)
		if 0 == temp.count():
			super(Photo,self).save()
		else:
			for p in temp:
				p.active = False
				p.save()
		super(Photo,self).save()
			
		
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
	title = models.CharField(max_length=50)
	content = models.TextField(blank=True)
	from_user = models.ForeignKey(User,related_name='from_u')
	to_user = models.ForeignKey(User,related_name='to_u')
	pub_date = models.DateTimeField()
	bool_read = models.BooleanField(default=False)
	parent = models.ForeignKey('self',blank=True,null=True)

	def __unicode__(self):
		return self.title




