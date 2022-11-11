from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article'),
    path('articles/home/style/featured/<int:num_posts>', views.ArticleJSONListView.as_view(), name="featured-articles" )
]