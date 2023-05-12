from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Team, TeamStatistic

@receiver(post_save, sender=Team)
def create_team_statistic(sender, instance, created, **kwargs):
    if created:
        TeamStatistic.objects.create(team=instance)