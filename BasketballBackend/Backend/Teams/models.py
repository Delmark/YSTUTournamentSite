from django.db import models
from django.core.validators import FileExtensionValidator

class Team(models.Model):
    name = models.CharField(verbose_name="Название команды", max_length=120, unique=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, verbose_name="Команда игрока", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя", max_length=120)
    last_name = models.CharField(verbose_name="Фамилия", max_length=120)
    middle_name = models.CharField(verbose_name="Отчество", blank=True, null=True, max_length=120)
    photo = models.ImageField(verbose_name='Фото игрока', blank=True, upload_to='player_photos/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

    def __str__(self):
        return f"{self.last_name} {self.name} {self.middle_name or ''}"

    @property
    def get_photo(self):
        if not self.photo:
            return 'media/images/placeholder.png'
        return self.photo.url

class TeamStatistic(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played_games = models.IntegerField(verbose_name="Сыграно игр", default=0, blank=True)
    wins = models.IntegerField(verbose_name="Победы", default=0, blank=True)
    draws = models.IntegerField(verbose_name="Ничьи", default=0, blank=True)
    losses = models.IntegerField(verbose_name="Поражения", default=0, blank=True)
    players = models.ManyToManyField(Player)

    def win_percentage(self):
        if self.played_games == 0:
            return 0
        else:
            return (self.wins + 0.5 * self.draws) / self.played_games * 100

    def __str__(self):
        return f"Статистика команды {self.team.name}"
