from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', views.docs, name='docs'),
    path('contacts/', views.contacts, name='contact'),
    path('archieve/', views.archieve, name='archieve'),
    path('results/', views.results, name='results'),
    path('news/', views.all_news, name='news'),
    path('news/<int:pk>/', views.news_detail, name='detail-article'),
    path('news/create_article/', views.create_news, name='create-article'),
    path('news/<int:pk>/delete/', views.delete_news, name='delete-article'),
]
