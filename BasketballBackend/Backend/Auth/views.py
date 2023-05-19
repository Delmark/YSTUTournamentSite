from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import TeamCreationForm, TeamStatisticCreationForm, PlayerCreationForm, MatchCreationForm
from .models import UserProfile, User
from urllib.parse import urlencode, urlparse
from django.contrib.auth.decorators import user_passes_test

def register(request):
    if request.method == 'POST':
        request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
        redirect_url = request.session.get('referer', 'News:index')

        if User.objects.filter(username=request.POST['username']).exists():
            params = {'error': 1}
            url = redirect_url + '?' + urlencode(params)
            return redirect(url)

        user = User.objects.create_user(
            username=request.POST['username'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password1']
        )

        profile = UserProfile.objects.create(
            user=user,
            middle_name=request.POST['middle_name'],
            birth_date=request.POST['birth_date']
        )

        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, user)

        return redirect(redirect_url)

def login_view(request):
    if request.method == 'POST':
        request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
        redirect_url = request.session.get('referer', 'News:index')


        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect(redirect_url)
        else:
            params = {'error': 2}
            url = redirect_url + '?' + urlencode(params)
            return redirect(url)

def logout_view(request): 
    logout(request)
    request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
    redirect_url = request.session.get('referer', 'index')
    return redirect(redirect_url)

@user_passes_test(lambda u: u.is_superuser)
def org_account(request):
    team_form = TeamCreationForm()
    team_statistic_form = TeamStatisticCreationForm()
    player_form = PlayerCreationForm()
    match_form = MatchCreationForm()

    if request.method == 'POST':
        if 'team' in request.POST:
            team_form = TeamCreationForm(request.POST)
            team_statistic_form = TeamStatisticCreationForm(request.POST, request.FILES)
            if team_form.is_valid() and team_statistic_form.is_valid():
                team = team_form.save()
                team_statistic = team_statistic_form.save(commit=False)
                team_statistic.team = team
                team_statistic.save()
                return HttpResponse("Успешно создано")
        elif 'player' in request.POST:
            player_form = PlayerCreationForm(request.POST, request.FILES)
            if player_form.is_valid():
                player_form.save()
                return HttpResponse("Успешно создано")
        elif 'match' in request.POST:
            match_form = MatchCreationForm(request.POST)
            if match_form.is_valid():
                match_form.save()
                return HttpResponse("Успешно создано")

    return render(request, 'org.html', {
        'team_form': team_form,
        'team_statistic_form': team_statistic_form,
        'player_form': player_form,
        'match_form': match_form,
    })

