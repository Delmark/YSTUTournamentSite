from django.contrib import admin
from .models import Team, TeamStatistic, Player


@admin.register(TeamStatistic)
class TeamStatisticAdmin(admin.ModelAdmin):
    list_display = ('team', 'played_games', 'wins', 'draws', 'losses', 'win_percentage')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'middle_name', 'team')
    list_filter = ('team',)
    search_fields = ('name', 'last_name', 'middle_name', 'team__name')
    ordering = ('last_name', 'name')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)