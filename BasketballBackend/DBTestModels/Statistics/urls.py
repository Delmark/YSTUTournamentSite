from .views import PlayerView, PlayerInfo
from django.urls import path
from . import views

urlpatterns = [
    path('', PlayerView.as_view(), name="players"),
    path('<int:pk>/',PlayerInfo.as_view(),name="player_info"),
    path('player_profile/', views.player_profile, name='player_profile'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', views.logoutv, name='logout'),
    path('admin/', views.admin_profile, name='admin_panel'),
]
