from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name', 'short_name', 'gsis_id')
    search_fields = ("name", )

@admin.register(PassingStats)
class Player(admin.ModelAdmin):
    list_display = ('gsis_id', 'season', 'week', )