from django.contrib import admin
from .models import AppComment, BlogComment

# Register your models here.

admin.site.register(AppComment)
admin.site.register(BlogComment)