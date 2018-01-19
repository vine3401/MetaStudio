from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'createTime', 'modifiedTime', 'category']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
