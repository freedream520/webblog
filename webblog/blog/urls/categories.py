from django.conf.urls.defaults import *
from django.views.generic.list import ListView
from blog.models import Category

category_info_dict = {
	'queryset':Category.objects.all(),
	}
		
urlpatterns = patterns('',
	url(r'$^',ListView.as_view(**category_info_dict),name='category_archive_index'),)
