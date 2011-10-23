from django.conf.urls.defaults import *
from django.conf import settings
import blog.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
	url(r'^blog/',include(blog.urls)),
)
