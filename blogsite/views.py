from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Poem,Music
# # Create your views here.
def index(request):
    poems = Poem.objects.order_by('-id')[:2]
    data = {
        'poems':poems
    }
    return render(request,'index.html',data)
def articles(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, "articles.html",context)
def article(request,id):
    article=Article.objects.get(id=id)
    context = {
        'article':article
    }
    return render(request, "article.html",context)

def poems(request)  :
    poems = Poem.objects.all()
    data = {
        'poems':poems
    }
    return render(request,'poems.html',data)
def poem(request,id):
    poem=Poem.objects.get(id=id)
    context = {
        'poem':poem
    }
    return render(request, "poem.html",context)
def music(request)  :
    music = Music.objects.all()
    data = {
        'music':music
    }
    return render(request,'music.html',data)