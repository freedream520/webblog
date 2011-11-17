from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.views.generic.simple import direct_to_template

from blog.urls import entries,links,categories
from tagging.urls import tags
from codeShare.urls import snippets
from people.urls import people_urls
from views import register,logout_page
from people.views import show_msg_by_id
#for friendship
from people.views import show_friend , friend_invite,friend_accept,make_friend,ignore_msg
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
	url(r'^people/',include(people_urls)),
	# for feed
	url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds_url_2_view}),
	# for login,logout,register
	url(r'^accounts/login/$',login),
	url(r'^accounts/logout/$',logout_page),
	url(r'^accounts/register/$',register),
	url(r'^accounts/profile/$',direct_to_template,{'template':'registration/welcome.html'}),
	url(r'^register/success/$',direct_to_template,{'template':'registration/success.html'}),
	# for message
	url(r'^msg/(?P<msg_id>\d+)/$',show_msg_by_id),
	url(r'^friends/$',show_friend),
	#url(r'^confirm/(\d+)/$',confirm_friendship),
	url(r'^ignore/(\d+)/$',ignore_msg),
	#url(r'^delete/(\d+)/$',delete_friendship),

	# friend invite
	url(r'^friend/invite/$',friend_invite),
	url('^friend/accept/(\w+)/$',friend_accept),
	url('^make/friend/$',make_friend),
	url(r'^err/$',direct_to_template,{'template':'show_error.html'}),
)


#for static files
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
