from django.contrib import admin
from .models import blogx , comment
# Register your models here.


class blogxAdmin(admin.ModelAdmin):
    list_display = ('blog_id','blog_name')

class commentAdmin(admin.ModelAdmin):
    list_display = ('cum_id','text')

admin.site.register(blogx,blogxAdmin)

admin.site.register(comment,commentAdmin)

