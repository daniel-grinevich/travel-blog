from django.shortcuts import render
from travelblog.articles.models import HomePage, Article, Media, Section
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.http import JsonResponse

"""
class Home(RetrieveAPIView):
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = HomePage.objects.all().filter(article__featured_home=True)
        serializer = HomePageSerializer(queryset,many=True)
        return Response({
            'serializer': serializer.data,
        })
"""
class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Article.objects.filter(featured_home=True)
        context['sections'] = HomePage.objects.all().order_by('-rank')
        context['hero'] = Media.objects.filter(
            homepage__style='H'
        )
        context['featured'] = Article.objects.filter(featured_home=True).filter(
            homepage__style='F'
        )[:2]
        context['recent'] = Article.objects.filter(featured_home=True).order_by('-created_at')[:6]
        context['scroll'] = Article.objects.filter(featured_home=True).filter(
            homepage__style='S'
        )[:7]
        context['city'] = Article.objects.filter(featured_home=True).filter(
            homepage__style='C'
        )[:10]
        return context

class ArticleJSONListView(View):
    def get(self, *args, **kwargs):
        upper_bound = kwargs.get('num_posts')
        lower_bound = upper_bound - 1
        data = list(Article.objects.filter(featured_home=True).filter(
            homepage__style='F').values()[lower_bound:upper_bound])
        return JsonResponse({'data':data}, safe=False)

def about(request):
    return render(request, 'about.html')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = Section.objects.filter(article__slug=self.kwargs.get('slug'))
        return context
    



    


