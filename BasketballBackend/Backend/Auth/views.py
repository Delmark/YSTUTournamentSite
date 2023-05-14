from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserProfile, User

from News.models import News, Photo
from Teams.models import TeamStatistic

def register(request):
    if request.method == 'POST':

        if User.objects.filter(username=request.POST['username']).exists():
            context = {'news': News.objects.order_by('pub_date')[:3],
               'photos': Photo.objects.order_by('pub_date')[:6],
               'teams': TeamStatistic.objects.order_by('rating').all(),
               'register_error_message': 'Такой пользователь уже существует'}
            return render(request, 'index.html', context)

        user = User.objects.create_user(
            username=request.POST['username'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password1']
        )

        profile = UserProfile.objects.create(
            user=user,
            middle_name=request.POST['middle_name'],
            birth_date=request.POST['birth_date']
        )

        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request, user)

        redirect_url = request.session.get('referer', 'index')
        return redirect(redirect_url)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            
            redirect_url = request.session.get('referer', 'index')
            return redirect(redirect_url)
        else:
            context = {'news': News.objects.order_by('pub_date')[:3],
               'photos': Photo.objects.order_by('pub_date')[:6],
               'teams': TeamStatistic.objects.order_by('rating').all(),
               'login_error_message': 'Неверный логин или пароль'}
            return render(request, 'index.html', context)

def logout_view(request): 
    logout(request)
    redirect_url = request.session.get('referer', 'index')
    return redirect(redirect_url)