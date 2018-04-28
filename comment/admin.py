from django.contrib import admin
from .models import GameComment, BlogComment

# Register your models here.

admin.site.register(GameComment)
admin.site.register(BlogComment)