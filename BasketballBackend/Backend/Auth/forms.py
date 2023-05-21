from django import forms
from Teams.models import Team, TeamStatistic, Player
from Games.models import Match

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class TeamStatisticCreationForm(forms.ModelForm):
    class Meta:
        model = TeamStatistic
        fields = ['logo', 'rating', 'played_games', 'wins', 'draws', 'losses']

class PlayerCreationForm(forms.ModelForm):
    middle_name = forms.CharField(label='Отчество', max_length=100, required=False)
    photo = forms.ImageField(label='Фото', required=False)
    
    class Meta:
        model = Player
        fields = ['team', 'name', 'last_name', 'middle_name', 'photo', 'height']

class MatchCreationForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team_1', 'team_2', 'date', 'time', 'place', 'season', 'is_finished', 'team_1_goals', 'team_2_goals']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }