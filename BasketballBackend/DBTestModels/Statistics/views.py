from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class PlayerInfo(DetailView):
    model = PlayerStats
    template_name = "playerdetail.html"
    context_object_name = "playerStats"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Страница игрока {{player.player_id.first_name}}"
        return context

def player_profile(request):
    player = Player.objects.get(user=request.user)
    player_stats = PlayerStats.objects.get(player=player)
    context = {
        'player': player,
        'player_stats': player_stats,
    }
    return render(request, 'player_profile.html', context)

def admin_profile(request):
    return render(request, 'admin_profile.html')

from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('player_profile')
            else:
                form.add_error(None, 'Incorrect username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})