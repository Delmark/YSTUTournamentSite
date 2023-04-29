from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist


from .models import Player, PlayerStats, User, News
from .forms import NewsForm

class PlayerView(ListView):
    model = Player
    template_name = "playerslist.html"
    context_object_name = "players"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Игроки"
        return context

def home(request):
    news = News.objects.all()
    context = {
        'articles': news,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def logoutv(request):
    logout(request)
    return redirect('home')

class PlayerInfo(DetailView):
    model = PlayerStats
    template_name = "playerdetail.html"
    context_object_name = "playerStats"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Страница игрока {{player.player_id.first_name}}"
        return context

def player_profile(request):
    try:
        player = Player.objects.get(user=request.user)
        player_stats = PlayerStats.objects.get(player=player)
        context = {
            'player': player,
            'player_stats': player_stats,
        }
        return render(request, 'player_profile.html', context)
    except ObjectDoesNotExist:
        return render(request, 'player_profile_no_stats.html')

from django.shortcuts import render
from .models import News

def admin_profile(request):
    news = News.objects.all()
    players = Player.objects.all()
    context = {
        'news': news,
        'players': players
    }
    return render(request, 'admin_profile.html', context)

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

class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='admin').exists():
            return '/admin_profile/'
        else:
            try:
                player = Player.objects.get(user=user)
            except ObjectDoesNotExist:
                return reverse('home')
            return '/player_profile/'