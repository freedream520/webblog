from django.conf.urls.defaults import *
from blog.models import Entry,Link
from django.views.generic.list import ListView
from tagging.models import Tag

tag_info_dict = {
	"queryset":Tag.objects.all(),
}

urlpatterns = patterns('',
	url(r'$^',ListView.as_view(**tag_info_dict),name='tag_list_index'),)
