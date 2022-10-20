"""travelblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from travelblog.drf import views as drfview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articles/category/all/', drfview.CategoryList.as_view()),
    path('api/articles/category/all/view/', drfview.CategoryListTemplate.as_view()),
    path('api/articles/all/', drfview.ArticleList.as_view()),
    path('api/articles/category/<str:query>/', drfview.ArticleByCategory.as_view()),
     path('api/articles/homepage/<str:query>/', drfview.ArticleByHomepageStyle.as_view()),
]

admin.site.site_header = f"Mili's admin protal"
admin.site.site_title = f"Mili's admin protal"
admin.site.index_title = "Hello Mili!"