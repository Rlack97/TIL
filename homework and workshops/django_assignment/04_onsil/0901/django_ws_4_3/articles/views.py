from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')


def detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)



def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')


def edit(request, id):
    article = Article.objects.get(id=id)
    context = {'article':article,}
    return render(request, 'articles/edit.html', context)


def update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.id)