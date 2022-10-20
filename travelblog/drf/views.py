from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from travelblog.articles.models import Category, Article
from travelblog.drf.serializer import CategorySerializer, ArticleSerializer

class CategoryList(APIView):
    """
    Return list of all categories
    """

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryListTemplate(RetrieveAPIView):
    queryset = Category.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_detail.html'

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response({'serializer': serializer.data})

class ArticleList(APIView):
    """
    Get all articles 
    """

    def get(self, request, query=None):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

class ArticleByCategory(APIView):
    """
    Get an article by the category 
    """

    def get(self, request, query=None):
        queryset = Article.objects.filter(category__slug=query)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

class ArticleByHomepageStyle(APIView):
    """
    Get an article by the homepage's style 
    """

    def get(self, request, query=None):
        queryset = Article.objects.filter(homepage__style=query)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)