from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from travelblog.articles.models import Category, Article
from travelblog.drf.serializer import CategorySerializer, ArticleSerializer


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def article(request):
    return render(request, 'article.html')
