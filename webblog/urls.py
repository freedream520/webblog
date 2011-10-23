from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
#import blog.urls.entries
#import blog.urls.links
from blog.urls import entries,links,categories
from tagging.urls import tags
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
	url(r'^$',direct_to_template,{'template':'index.html'}),
	url(r'^entry/',include(entries)),
	url(r'^link/',include(links)),
	url(r'^category/',include(categories)),
	url(r'^tag/',include(tags)),
)
