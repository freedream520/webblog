from django.db import models 
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from tagging.fields import TagField
from markdown import markdown

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=250,help_text='MAx 250 chars')
	slug = models.SlugField(unique=True,help_text='suggested value automatically generated form title. must be unique.')
	description = models.TextField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return "/categories/%s/" % self.slug

class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager,self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS,'Live'),
		(DRAFT_STATUS,'Draft'),
		(HIDDEN_STATUS,'Hidden'),
	)
	# core fields	
	title = models.CharField(max_length=250,help_text='max to 250 chars')
	excerpt = models.TextField(blank=True,help_text='a short summary of the entry , optinal')
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.now)
	# store html fields 
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html = models.TextField(editable=False, blank=True)
	#meta data
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	slug = models.SlugField(unique_for_date='pub_date')
	status = models.IntegerField(choices=STATUS_CHOICES,default=LIVE_STATUS)
	#categories fields
	categories = models.ManyToManyField(Category)
	tags = TagField()
	
	objects = models.Manager()
	live = LiveEntryManager()

	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry,self).save()
	
	class Meta:
		verbose_name_plural = "Entries"
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/%s/%s/%s/%s/"%(self.pub_date.strftime("%Y"),self.pub_date.strftime("%b").lower(),self.pub_date.strftime("%d"),self.slug)
#		return ('blog_entry_detail',(),{
#			'year':self.pub_date.strftime("%Y"),
#			'month':self.pub_date.strftime("%b").lower(),
#			'day':self.pub_date.strftime("%d"),
#			'slug':self.slug })


class Link(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	description_html = models.TextField(blank=True)
	url = models.URLField(unique=True)
	posted_by = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.now)
	slug = models.SlugField(unique_for_date='pub_date')
	tags = TagField()
	enable_comments = models.BooleanField(default=False)
	post_elsewhere = models.BooleanField('Post to del.icio.us',default=True,help_text='if checked ,this link will be posted both to your blog and to your del.icio.us account.')
	via_name = models.CharField('Via',max_length=250,blank=True,help_text='the name of the person whos site you spotted the link on .Optional')
	via_url = models.URLField('Via URL',blank=True,help_text='the url of the site where you spotted the link .Optional')

	class Meta:
		ordering = ['-pub_date']

	def __unicode__(self):
		return self.title 
	
	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		if not self.id and self.post_elsewhere:
		#	import pydelicious
		#	from django.utils.encoding import smart_str
		#	pydelicious.add(settings.DELICIOUS_USER,settings.DELICIOUS_PASSWORD,smart_str(self.url),smart_str(self.title),smart_str(self.tags))
			pass
		super(Link,self).save()

	def get_absolute_url(self):
		return "/url/%s/%s/%s/%s/"%(self.pub_date.strftime("%Y"),self.pub_date.strftime("%b").lower(),self.pub_date.strftime("%d"),self.slug)
