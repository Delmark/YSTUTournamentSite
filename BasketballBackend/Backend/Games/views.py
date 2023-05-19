from django.shortcuts import render, HttpResponse
from .models import Match
from django.db.models import Q
from Teams.models import TeamStatistic

def schedule(request):
    return render(request, 'schedule.html')

def archieve(request):
    season = request.GET.get('season')
    match_id = request.GET.get('match')

    matches = Match.objects.all()

    if season and match_id:
        matches = matches.filter(season=season, id=match_id)
    elif season:
        matches = matches.filter(season=season)
    elif match_id:
        matches = matches.filter(id=match_id)

    team_statistics = None

    if len(matches) == 0:
        team_statistics = []
    elif len(matches) == 1:
        match = matches.first()
        team_statistics = TeamStatistic.objects.filter(Q(team=match.team_1) | Q(team=match.team_2))
    else:
        team_statistics = TeamStatistic.objects.filter(
            *[Q(team=match.team_1) | Q(team=match.team_2) for match in matches]
        )

    return render(request, 'archieve.html', {'matches': matches, 'team_statistics': team_statistics})