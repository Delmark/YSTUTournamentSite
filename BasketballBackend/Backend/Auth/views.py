from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        otchestvo = request.POST['otchestvo']
        birth_date = request.POST['birth_date']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']

            # Create user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            otchestvo=otchestvo,
            birth_date=birth_date,
            email=email,
            username=username,
            password=password1)
            
        login(request, user)
        return redirect('home')
    return render(request, 'index.html')  

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'index.html')

def logout_view(request): 
    logout(request)
    return redirect('home')