from django.contrib import admin
from codeShare.models import *


#class entryAdmin(admin.ModelAdmin):
#	prepopulated_fields = {"slug":("title",)}
#admin.site.register(Category,categoryAdmin)
#admin.site.register(Entry,entryAdmin)
#admin.site.register(Link)
admin.site.register(Language)
admin.site.register(Snippet)
