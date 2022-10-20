from django.contrib import admin
from travelblog.articles.models import Article, Section, City, Country, Link, Media, Category
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminBase
from mptt.admin import MPTTModelAdmin
# class SectionAdmin(SortableInlineAdminMixin, admin.StackedInline):
#     list_display = ('header','body')
#     model = Section


class SectionAdmin(admin.StackedInline):
    list_display = ('header','body','rank')
    model = Section

class LinkAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('header','body')
    model = Link

class ArticleBaseAdmin(SortableAdminBase,admin.ModelAdmin):
    list_display = ('title','body','is_visible','featured_home','country','city')
    list_filter = ('is_visible','featured_home','created_at')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SectionAdmin
    ]

    actions = [
        'hide_article_from_blog',
        'show_article_on_blog',
        'hide_article_from_homepage',
        'show_article_on_homepage',
    ]

    def hide_article_from_blog(self,request,queryset):
        queryset.update(is_visible = False)
        return

    def show_article_on_blog(self,request,queryset):
        queryset.update(is_visible = True)
        return

    def hide_article_from_homepage(self,request,queryset):
        queryset.update(featured_home = True)
        return

    def show_article_on_homepage(self,request,queryset):
        queryset.update(featured_home = True)
        return

class SectionBaseAdmin(SortableAdminBase,admin.ModelAdmin):
    list_display = ('header','body','article')
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
admin.site.register(Article, ArticleBaseAdmin)
admin.site.register(Section, SectionBaseAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Media)
admin.site.register(Category, MPTTModelAdmin)

