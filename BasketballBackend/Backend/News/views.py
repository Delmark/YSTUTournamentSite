from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.order_by('pub_date')[:3]
    context = {'news': news}
    return render(request, 'index.html', context)
