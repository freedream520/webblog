from django.template import Library
from django import template
from blog.models import Entry


register = Library()
# the tag name for the template files . like {% the_tag_name %}
# set it : get_lastest_entries

# the function for the template tag when it was called .
@register.inclusion_tag('blog/lastest_10_entries.html',takes_context=True)
def get_lastest_entries(context,number=10):
	entries = Entry.objects.all().order_by('-id')
	if number > len(entries):
		number = len(entries)
	return {'lastest_10':entries[:number]}

