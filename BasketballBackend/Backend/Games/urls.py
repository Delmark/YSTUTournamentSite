from django.urls import path
from . import views

app_name = 'Games'

urlpatterns = [
    path('', views.schedule, name="schedule"),
    path('archieve/', views.archieve, name='archieve'),
]
