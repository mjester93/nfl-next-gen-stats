from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name', 'short_name', 'gsis_id')
    search_fields = ("full_name", )

@admin.register(PassingStats)
class PassingStatsAdmin(admin.ModelAdmin):
    list_display = ('gsis_id', 'season', 'week', )

@admin.register(RushingStats)
class RushingStatsAdmin(admin.ModelAdmin):
    list_display = ('gsis_id', 'season', 'week', )

@admin.register(ReceivingStats)
class ReceivingStatsAdmin(admin.ModelAdmin):
    list_display = ('gsis_id', 'season', 'week', )