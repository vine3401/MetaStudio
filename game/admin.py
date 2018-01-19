from django.contrib import admin
from .models import GameCategory, Game
# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ['name','author','createTime', 'times', 'version']

admin.site.register(Game,GameAdmin)
admin.site.register(GameCategory)