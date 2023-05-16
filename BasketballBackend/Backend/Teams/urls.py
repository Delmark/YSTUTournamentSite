from django.urls import path
from . import views

app_name = 'Teams'

urlpatterns = [
    path('', views.teams, name='teams'),
    path('<int:team_id>/', views.team_detail, name='team-detail')
]
