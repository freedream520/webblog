from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.views.generic.dates import ArchiveIndexView
from blog.models import Entry
# Create your views here.

def entries_index(request):
	variables = RequestContext(request,{'entry_list':Entry.objects.all()})
	return render_to_response('blog/entry_index.html',variables)

def entry_detail(request,year,month,day,slug):
	import datetime,time
	date_stamp = time.strptime(year+month+day,"%Y%b%d")
	pub_date = datetime.date(*date_stamp[:3])
	entry = get_object_or_404(Entry,pub_date__year=pub_date.year,pub_date__month=pub_date.month,pub_date__day=pub_date.day,slug=slug)
	variables = (request,{'entry':entry})
	return render_to_response('blog/entry_detail.html',variables)

class my_index_view(TemplateView):
	template_name = "hello.html"

	def get_context_data(self,**kwargs):
		return {
			'greeted':'world'
			}
