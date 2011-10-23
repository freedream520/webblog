from django.conf.urls.defaults import *
from django.views.generic.dates import *
from blog.models import Entry

entry_info_dict = {
	'queryset':Entry.objects.all(),
	'paginate_by':10,
	'allow_empty':True,
	'date_field':'pub_date',
	}

entry_info_dict_year = {
	'queryset':Entry.objects.all(),
	'paginate_by':10,
	'allow_empty':True,
	'date_field':'pub_date',
	'make_object_list':True,
	}


entry_info_dict_detail = {
	'queryset':Entry.objects.all(),
	'date_field':'pub_date',
}

urlpatterns = patterns('',
	url(r'$^',ArchiveIndexView.as_view(**entry_info_dict),name='entry_archive_index'),
	url(r'^(?P<year>\d{4})/$',YearArchiveView.as_view(**entry_info_dict_year),name='entry_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',MonthArchiveView.as_view(**entry_info_dict),name='entry_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',DayArchiveView.as_view(**entry_info_dict),name='entry_archive_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',DateDetailView.as_view(**entry_info_dict_detail),name='entry_archive_detail'),
)

