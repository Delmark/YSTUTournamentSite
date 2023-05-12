from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Team(models.Model):
    team_id = models.AutoField(verbose_name='ID Команды', primary_key=True)
    team_name = models.CharField(verbose_name='Название команды', max_length=255,null=False)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    player_id = models.AutoField(verbose_name='ID Игрока',primary_key=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    team_id = models.ForeignKey(Team, verbose_name='ID Команды', on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='Имя', max_length=255,null=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия',null=True)
    age = models.IntegerField(verbose_name='Возраст', null=False)
    photo = models.ImageField(verbose_name='Фото', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.team_id.team_name}'

    
class PlayerStats(models.Model):
    player = models.ForeignKey(Player, verbose_name=("ID игрока"), on_delete=models.CASCADE)
    games_played = models.IntegerField(verbose_name="Сыграно игр", default=0)
    total_score = models.IntegerField(verbose_name="Всего очков", default=0)
    
    def __str__(self) -> str:
        return f"Статистика игрока {self.player.first_name + self.player.last_name}"
    
    def average_score_count(self):
        if self.total_score == 0:
            return 0
        return self.games_played/self.total_score