from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from .forms import NewsCreateForm, ArticleImageForm, ArticleImageFormset
from .models import News, Photo, ArticleImage, Partner
from Teams.models import TeamStatistic, Team
from Games.models import Match

def index(request):
    news = News.objects.order_by('-pub_date')[:3]
    photo = Photo.objects.order_by('-pub_date')[:6]
    teams = TeamStatistic.objects.order_by('rating').all()[:10]

    context = {'news': news,
        'photos': photo,
        'teams': teams}

    if 'error' in request.GET:
        error_type = request.GET.get('error')
        if error_type == 2:
            context.update({'login_error_message': "Неверный логин или пароль"})
            return render(request, 'index.html', context)
        else:
            context.update({'register_error_message': "Неверный логин или пароль"})
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)

@user_passes_test(lambda user: user.is_superuser)
def create_news(request):
    form = NewsCreateForm()
    formset = ArticleImageFormset()
    if request.method == 'POST':
        form = NewsCreateForm(request.POST, request.FILES)
        formset = ArticleImageFormset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            news = form.save()
            for form in formset:
                if form.cleaned_data.get('image'):
                    ArticleImage.objects.create(article=news, image=form.cleaned_data.get('image'))
            return redirect('detail-article', pk=news.pk)
    return render(request, 'news/create-article.html', {'form': form, 'formset': formset})

@user_passes_test(lambda user: user.is_superuser)
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect(reverse('news'))

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    images = news.images.all()
    return render(request, 'news/detail-article.html', {'news': news, 'images': images})

def all_news(request):
    news = News.objects.order_by('-pub_date')
    return render(request, 'news/news-page.html', {'news': news})


def contacts(request):
    partners = Partner.objects.all()
    return render(request, 'contacts.html', {'partners': partners})

def docs(request):
    return render(request, 'docs.html')

def results(request):
    teams = Team.objects.all()
    team_filter = request.GET.get("team")
    
    if team_filter:
        matches = Match.objects.filter(Q(team_1__name=team_filter) | Q(team_2__name=team_filter))
    else:
        matches = Match.objects.filter(is_finished=True).order_by('date')
    return render(request, 'results.html', {'teams': teams, 'matches': matches})
