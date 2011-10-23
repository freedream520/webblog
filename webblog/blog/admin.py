from django.contrib import admin
from blog.models import *

class categoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}

class entryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug":("title",)}

admin.site.register(Category,categoryAdmin)
admin.site.register(Entry,entryAdmin)
admin.site.register(Link)
