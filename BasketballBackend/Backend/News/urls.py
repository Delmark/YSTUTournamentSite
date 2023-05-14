from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', views.docs, name='docs'),
    path('contacts/', views.contacts, name='contact'),
    path('archieve/', views.archieve, name='archieve'),
    path('results/', views.results, name='results')
]
