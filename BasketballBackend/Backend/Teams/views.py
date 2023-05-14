from django.shortcuts import render, HttpResponse

def teams(request):
    return render(request, 'teams.html')
