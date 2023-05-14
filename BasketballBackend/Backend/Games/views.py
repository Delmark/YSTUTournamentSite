from django.shortcuts import render, HttpResponse

def schedule(request):
    return render(request, 'schedule.html')