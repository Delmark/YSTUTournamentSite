from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Player, PlayerStats

class PlayerView(ListView):
    model = Player
    template_name = "playerslist.html"
    context_object_name = "players"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Игроки"
        return context

class PlayerInfo(DetailView):
    model = PlayerStats
    template_name = "playerdetail.html"
    context_object_name = "player"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Страница игрока {{player.player_id.first_name}}"
        return context