from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'createTime', 'modifiedTime', 'category', 'author']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
