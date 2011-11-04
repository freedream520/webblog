from django.conf.urls.defaults import *
from codeShare.models import Snippet
from codeShare.views import show_all

urlpatterns = patterns('',url(r'^$',show_all),)
