from travelblog.articles.models import Category, Article
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
            fields = ['title','slug']
            read_only = True
            editable = False