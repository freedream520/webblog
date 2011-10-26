from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf.urls.static import static
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
	url(r'^comments/',include('django.contrib.comments.urls')),
)


#for static files
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
