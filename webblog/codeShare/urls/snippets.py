from django.conf.urls.defaults import *
from codeShare.models import Snippet
from codeShare.views import show_all,show_snippet_by_id,show_by_lang

urlpatterns = patterns('',
			url(r'^$',show_all),
			url(r'^(\d+)/$',show_snippet_by_id),
			url(r'^lang/(\d+)/$',show_by_lang),
			)
