from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static

from blog.urls import entries,links,categories
from tagging.urls import tags
from codeShare.urls import snippets

#for feed
from blog.feed import *
feeds_url_2_view = {
	'recent':RecentEntries
}

urlpatterns = patterns('',
	url(r'^admin/',include(admin.site.urls)),
	url(r'^$',direct_to_template,{'template':'index.html'}),
	url(r'^entry/',include(entries)),
	url(r'^link/',include(links)),
	url(r'^category/',include(categories)),
	url(r'^tag/',include(tags)),
	url(r'^snippet/',include(snippets)),
	url(r'^comments/',include('django.contrib.comments.urls')),
	# for feed
	url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds_url_2_view}),
)


#for static files
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
