from django.contrib import admin
from travelblog.articles.models import Article, Country, City
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminBase


class ArticleAdmin(SortableAdminBase, admin.ModelAdmin):
    list_diplay = ('title')
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Country)
admin.site.register(City)