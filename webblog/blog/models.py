from django.db import models 
from django.contrib.auth.models import User
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
		return ('blog_entry_detail',(),{
			'year':self.pub_date.strftime("%Y"),
			'month':self.pub_date.strftime("%b").lower(),
			'day':self.pub_date.strftime("%d"),
			'slug':self.slug })

	get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	description_html = models.TextField(blank=True)
	url = models.URLField(unique=True)
	posted_by = models.ForeignKey(User)

