from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Match
from django.db.models import Q
from Teams.models import TeamStatistic, Team

def schedule(request):
    matches = Match.objects.filter(date__gte=datetime.today(), is_finished=False).order_by('date')
    team_filter = request.GET.get('team')
    all_matches = matches
    if team_filter:
        matches = matches.filter(Q(team_1__name=team_filter) | Q(team_2__name=team_filter))
    return render(request, 'schedule.html', {'matches': matches, 'teams': Team.objects.all(), 'team_filter': team_filter, 'all_matches': all_matches})

def archieve(request):
    season = request.GET.get('season')
    match_id = request.GET.get('match')

    matches = Match.objects.filter(is_finished=True)

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