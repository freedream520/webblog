from django.contrib import admin
from people.models import *

admin.site.register(People)
admin.site.register(Photo)
admin.site.register(Department)
admin.site.register(Msg)
admin.site.register(FriendShip)
admin.site.register(Invitation)

