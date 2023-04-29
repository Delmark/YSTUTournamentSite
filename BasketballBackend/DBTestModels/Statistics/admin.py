from django.contrib import admin
from django.shortcuts import render, redirect

from .models import Player,Team, PlayerStats, News

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(PlayerStats)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

from .forms import NewsForm

def admin_profile(request):
    news = News.objects.all()
    form = NewsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    context = {
        'news': news,
        'form': form,
    }
    return render(request, 'admin_profile.html', context)