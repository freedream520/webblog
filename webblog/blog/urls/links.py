from django.conf.urls.defaults import *
from django.views.generic.dates import *
from blog.models import Link

link_info_dict = {
	'queryset':Link.objects.all(),
	'date_field':'pub_date',
	}
		
urlpatterns = patterns('',
	url(r'$^',ArchiveIndexView.as_view(**link_info_dict),name='link_archive_index'),)
