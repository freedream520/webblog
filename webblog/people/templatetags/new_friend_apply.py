from django.template import Library
#from people.models import FriendShip
from people.models import Invitation,Msg

register = Library()

@register.inclusion_tag('people/new_friend_apply.html',takes_context=True)
def get_new_friend_apply_list(context,u_id):
	## retrial from the msg where type= friend. the destiny is my_id.
	## obj_cnt is queryed from the table invitation that the receiver is my_id
	## and the obj_list is the msg that send me the accept link to add  friends.
	
	obj_cnt = Invitation.objects.all().filter(receiver=u_id)
	obj_list = Msg.objects.all().filter(to_user = u_id , msg_type=3) ## 3 stands for the firend type. 
	
	return {'obj_list':obj_list,'obj_cnt':len(obj_list),}
