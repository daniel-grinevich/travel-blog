from itertools import product
from unicodedata import category
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

class ArticleByCategory(APIView):
    """
    Get an article by the category 
    """

    def get(self, request, query=None):
        queryset = Article.objects.filter(category__slug=query)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)