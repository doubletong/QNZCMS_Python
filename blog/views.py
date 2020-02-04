from django.shortcuts import render
from .models import Article
from django.utils.translation import gettext as _

def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles': articles})

def single(request,id):
    single = Article.objects.get(id=id)
    return render(request,'single.html',{'single': single})


def test(request):
    context={
        'hello':_('Hello')
    }
    return render(request,'test.html',context)