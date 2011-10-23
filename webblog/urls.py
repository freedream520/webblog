from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
#import blog.urls.entries
#import blog.urls.links
from blog.urls import entries,links,categories,tags
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
	url(r'^blog/',include(entries)),
	url(r'^link/',include(links)),
	url(r'^category/',include(categories)),
	url(r'^tags/',include(tags)),
)
