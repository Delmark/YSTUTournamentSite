from django.apps import AppConfig


class TeamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Teams'

    def ready(self):
        import Teams.signals