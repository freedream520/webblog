from django.template import Library
from people.models import People,Msg

register = Library()

@register.inclusion_tag('people/msg_box.html',takes_context=True)
def msg_box_list(context,user_id):
	msg_list =  Msg.objects.all().filter(to_user = user_id )
	return {'msg_list':msg_list}		


