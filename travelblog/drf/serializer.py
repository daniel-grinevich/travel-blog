from asyncio import AbstractChildWatcher
from travelblog.articles.models import Category, Article, HomePage
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','slug']
        read_only = True
        editable = False

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
            model = Article
            fields = '__all__'
            read_only = True
            editable = False
            depth = 2

class HomePageSerializer(serializers.ModelSerializer):

    article = ArticleSerializer(many=True)
    class Meta:
            model = HomePage
            fields = [
                'header',
                'subheader',
                'style',
                'rank',
                'article',
            ]
            read_only = True
            editable = False