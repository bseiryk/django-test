from django.contrib import admin

from .models import Items


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name', 'parent', 'is_root', 'is_deleted', 'type')
    list_display_links = ['name']


admin.site.register(Items, ItemsAdmin)
