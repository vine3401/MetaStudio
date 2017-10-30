from django.contrib import admin
from .models import AppCategory, App
# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ['name','author','createTime', 'times', 'version']

admin.site.register(App,AppAdmin)
admin.site.register(AppCategory)