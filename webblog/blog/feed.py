from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site
from blog.models import Entry

current_site = Site.objects.get_current()

class RecentEntries(Feed):
	title = 'Webblog Entry | Recent Entries' 
	link = '/recent/entry/'
	description = 'Recent entries posted on the Webblog'

	def items(self):
		return Entry.objects.order_by('-id')[:10]
