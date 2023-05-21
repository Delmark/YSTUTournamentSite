from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Team, TeamStatistic
def teams(request):
    teams = Team.objects.all()
    query = request.GET.get('search')
    if query:
        teams = teams.filter(name__icontains=query)
    return render(request, 'teams.html', {'teams': teams, 'query': query})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_statistic = TeamStatistic.objects.get(team=team)
    players = team.player_set.all()
    matches = team.team_1_matches.filter(is_finished=False) | team.team_2_matches.filter(is_finished=False)
    return render(request, 'team-pages/team-page.html', {'team': team, 'statistic': team_statistic, 'players': players, 'matches': matches})