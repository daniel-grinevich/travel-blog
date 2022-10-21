from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from travelblog.articles.models import HomePage, Article
from travelblog.drf.serializer import ArticleSerializer, HomePageSerializer


class Home(RetrieveAPIView):

    """"
    get homepage styles with active articles
    """
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, query=None):
        queryset = HomePage.objects.all()
        serializer_home = HomePageSerializer(queryset,many=True)
        queryset = Article.objects.filter(featured_home=True)
        serializer_article = ArticleSerializer(queryset,many=True)
        return Response({
            'serializer_home': serializer_home.data,
            'serailizer_article': serializer_article,
        })
        
def about(request):
    return render(request, 'about.html')

def article(request):
    return render(request, 'article.html')
