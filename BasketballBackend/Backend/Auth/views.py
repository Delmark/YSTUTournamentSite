from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import UserProfile, User
from urllib.parse import urlencode, urlparse

def register(request):
    if request.method == 'POST':
        request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
        redirect_url = request.session.get('referer', 'News:index')

        if User.objects.filter(username=request.POST['username']).exists():
            params = {'error': 1}
            url = redirect_url + '?' + urlencode(params)
            return redirect(url)

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

        return redirect(redirect_url)

def login_view(request):
    if request.method == 'POST':
        request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
        redirect_url = request.session.get('referer', 'News:index')


        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect(redirect_url)
        else:
            params = {'error': 2}
            url = redirect_url + '?' + urlencode(params)
            return redirect(url)

def logout_view(request): 
    logout(request)
    request.session['referer'] = request.META.get('HTTP_REFERER', 'News:index')
    redirect_url = request.session.get('referer', 'index')
    return redirect(redirect_url)