from django.urls import path
from . import views

app_name = 'Teams'

urlpatterns = [
    path('teams/', views.teams, name='teams')
]
