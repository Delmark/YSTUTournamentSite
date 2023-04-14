from .views import PlayerView, PlayerInfo
from django.urls import path

urlpatterns = [
    path('', PlayerView.as_view(), name="players"),
    path('<int:pk>/',PlayerInfo.as_view(),name="player_info")
]
