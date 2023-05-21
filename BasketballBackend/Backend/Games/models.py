from django.db import models
from Teams.models import Team

class Match(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1_matches')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2_matches')
    date = models.DateField(verbose_name='Дата проведения матча')
    time = models.TimeField(verbose_name='Время проведения матча', null=True)
    place = models.CharField(verbose_name='Место проведения матча', max_length=150)
    season = models.PositiveIntegerField(verbose_name='Номер сезона')
    is_finished = models.BooleanField(verbose_name='Завершен ли матч', default=False)
    team_1_goals = models.PositiveIntegerField(verbose_name='Количество очков первой команды', default=0)
    team_2_goals = models.PositiveIntegerField(verbose_name='Количество очков второй команды', default=0)

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} ({self.date} {self.time})"