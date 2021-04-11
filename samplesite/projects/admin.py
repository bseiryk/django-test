from django.contrib import admin

from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name', 'is_deleted', 'root_folder')
    list_display_links = ['name']


admin.site.register(Projects, ProjectsAdmin)