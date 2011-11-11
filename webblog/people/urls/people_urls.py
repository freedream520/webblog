from django.conf.urls.defaults import *
from django.views.generic.dates import *
from people.views import show_people_by_id,show_all_people
from people.models import People

people_info_dict = {
	'queryset':People.objects.all(),
	}
		
urlpatterns = patterns('',
	url(r'$^',show_all_people),
	url(r'(?P<p_id>\d+)/$',show_people_by_id),
	)
