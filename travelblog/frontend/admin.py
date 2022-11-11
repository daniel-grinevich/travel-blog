from django.contrib import admin
from travelblog.frontend.models import HomePage, NavLink
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
    
# Register your models here.


class HomeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('header','style')
 



admin.site.register(HomePage, HomeAdmin)
admin.site.register(NavLink)
