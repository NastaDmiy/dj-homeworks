from django.shortcuts import render
from .models import Article

def show_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)