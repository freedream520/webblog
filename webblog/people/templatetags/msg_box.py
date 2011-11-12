from django.template import Library
from people.models import People,Msg

register = Library()

@register.inclusion_tag('people/msg_list.html',takes_context=True)
def get_msg_list(context,user_id):
	msg_list =  Msg.objects.all().filter(to_user = user_id )
	return {'msg_list':msg_list}		

@register.inclusion_tag('people/msg_count.html',takes_context=True)
def get_msg_count(context,user_id):
	msg_list=  Msg.objects.all().filter(to_user = user_id )
	return {'msg_cnt':len(msg_list)}		

@register.inclusion_tag('people/msg_box.html',takes_context=True)
def get_msg_new(context,user_id):
	msg_new =  Msg.objects.all().filter(to_user = user_id,bool_read = False)
	leng = msg_new.count()
	return {'msg_new':msg_new,'msg_cnt':len(msg_new)}
	

