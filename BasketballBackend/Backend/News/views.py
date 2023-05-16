from django.shortcuts import render
from .models import News, Photo
from Teams.models import TeamStatistic

def index(request):
    news = News.objects.order_by('pub_date')[:3]
    photo = Photo.objects.order_by('pub_date')[:6]
    teams = TeamStatistic.objects.order_by('rating').all()
    if 'error' in request.GET:
        error_type = request.GET.get('error')
        if error_type == 2:
            context = {'news': news,
           'photos': photo,
           'teams': teams,
           'login_error_message': "Неверный логин или пароль"}
            return render(request, 'index.html', context)
        else:
            context = {'news': news,
            'photos': photo,
            'teams': teams,
            'register_error_message': "Неверный логин или пароль"}
            return render(request, 'index.html', context)
    else:
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