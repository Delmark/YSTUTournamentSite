from django.shortcuts import render
from .models import News, Photo
from Teams.models import TeamStatistic

def index(request):
    news = News.objects.order_by('pub_date')[:3]
    photo = Photo.objects.order_by('pub_date')[:6]
    teams = TeamStatistic.objects.order_by('rating').all()
    context = {'news': news,
               'photos': photo,
               'teams': teams}
    return render(request, 'index.html', context)

def contacts(request):
    return render(request, 'contacts.html')

def docs(request):
    return render(request, 'docs.html')

def results(request):
    return render(request, 'results.html')

def archieve(request):
    return render(request, 'archieve.html')