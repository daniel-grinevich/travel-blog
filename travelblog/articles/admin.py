from django.contrib import admin
from travelblog.articles.models import Article, Section, City, Country, Link, Media, Category
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminBase
from mptt.admin import MPTTModelAdmin
# class SectionAdmin(SortableInlineAdminMixin, admin.StackedInline):
#     list_display = ('header','body')
#     model = Section


class SectionAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('header','body')
    model = Section

class LinkAdmin(SortableInlineAdminMixin, admin.StackedInline):
    list_display = ('header','body')
    model = Link

class ArticleBaseAdmin(SortableAdminBase,admin.ModelAdmin):
    list_display = ('title','body')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SectionAdmin
    ]

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

