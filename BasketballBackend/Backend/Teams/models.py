from django.db import models
from django.core.validators import FileExtensionValidator
from Auth.models import UserProfile

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
    user_profile = models.ForeignKey(UserProfile, related_name='players', on_delete=models.SET_NULL, null=True, blank=True)
    height = models.PositiveIntegerField(verbose_name="Рост", blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.name} {self.middle_name or ''}"

    @property
    def get_photo(self):
        if not self.photo:
            return 'media/images/placeholder.png'
        return self.photo.url
    
    @property
    def get_full_name(self):
        return f'{self.last_name} {self.name}'

class TeamStatistic(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    logo = models.ImageField(verbose_name="Логотип команды", upload_to='teams/logos/', blank=True)
    rating = models.IntegerField(verbose_name = "Рейтинг команды", default=0, blank=True)
    played_games = models.IntegerField(verbose_name="Сыграно игр", default=0, blank=True)
    wins = models.IntegerField(verbose_name="Победы", default=0, blank=True)
    draws = models.IntegerField(verbose_name="Ничьи", default=0, blank=True)
    losses = models.IntegerField(verbose_name="Поражения", default=0, blank=True)

    @property
    def get_logo(self):
        if not self.logo:
            return 'media/images/placeholder.png'
        return self.logo.url

    def win_percentage(self):
        if self.played_games == 0:
            return 0
        else:
            return (self.wins + 0.5 * self.draws) / self.played_games * 100

    def __str__(self):
        return f"Статистика команды {self.team.name}"
