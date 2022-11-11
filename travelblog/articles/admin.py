from django.contrib import admin
from travelblog.articles.models import Article, Section, City, Country, Link, Media, Category
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminBase,SortableAdminMixin
from mptt.admin import MPTTModelAdmin
from travelblog.frontend.models import HomePage
# class SectionAdmin(SortableInlineAdminMixin, admin.StackedInline):
#     list_display = ('header','body')
#     model = Section


class SectionAdmin(SortableInlineAdminMixin,admin.StackedInline):
    list_display = ('rank','header','body')
    model = Section

class LinkAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('slug','text')
    model = Link

class ArticleBaseAdmin(SortableAdminMixin, SortableAdminBase,admin.ModelAdmin):
    list_display = ('title','country','city','is_visible','featured_home', 'homepage')
    list_filter = ('is_visible','featured_home','created_at','homepage__style')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    inlines = [
        SectionAdmin
    ]

    actions = [
        'hide_article_from_blog',
        'show_article_on_blog',
        'hide_article_from_homepage',
        'show_article_on_homepage',
        'article_to_featured_section',
    ]

    def hide_article_from_blog(self,request,queryset):
        queryset.update(is_visible = False)
        return

    def show_article_on_blog(self,request,queryset):
        queryset.update(is_visible = True)
        return

    def hide_article_from_homepage(self,request,queryset):
        queryset.update(featured_home = False)
        return

    def show_article_on_homepage(self,request,queryset):
        queryset.update(featured_home = True)
        return
    
    def article_to_featured_section(self,request,queryset):
        feature = HomePage.objects.get(style='F')
        queryset.update(homepage=feature)
        return

class SectionBaseAdmin(SortableAdminMixin,SortableAdminBase,admin.ModelAdmin):
    list_display = ('header','body','article')
    search_fields = ['article__title']
    inlines = [
        LinkAdmin
    ]



# class ArticleAdmin(SortableAdminBase, admin.ModelAdmin):
#     list_diplay = ('title', 'created_timestamp')
#     prepopulated_fields = {'slug': ('title',)}
#     inline = [
#         CreditAdmin
#     ]


# Register your models here.
admin.site.register(Link)
admin.site.register(Article, ArticleBaseAdmin)
admin.site.register(Section, SectionBaseAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Media)
admin.site.register(Category, MPTTModelAdmin)

