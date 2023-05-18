from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_1', 'team_2', 'date', 'time', 'place', 'season', 'is_finished', 'team_1_goals', 'team_2_goals')
    list_filter = ('season', 'is_finished')
    search_fields = ('team_1__name', 'team_2__name', 'place')