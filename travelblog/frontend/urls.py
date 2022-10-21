from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('article', views.article, name='article'),
]