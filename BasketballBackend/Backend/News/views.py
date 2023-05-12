from django.shortcuts import render
from .models import News, Photo

def index(request):
    news = News.objects.order_by('pub_date')[:3]
    photo = Photo.objects.order_by('pub_date')[:6]
    context = {'news': news,
               'photos': photo}
    return render(request, 'index.html', context)
