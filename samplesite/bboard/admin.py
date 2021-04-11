from django.contrib import admin

from .models import (
    Bd,
    Rubric,
    Profile,
    Technology,
    Expertise,
    Education
)


class BbAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'title', 'content', 'price', 'rubric', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class RubricAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name')
    list_display_links = ['name']


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name')
    list_display_links = ['name']


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name')
    list_display_links = ['name']


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk', 'name')
    list_display_links = ['name']


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pk',
        'name',
        'surname',
        'salary_min',
        'email',
        'is_hired',
        'birth_date',
        'expertise',
        'education',
    )
    list_display_links = ['name']


admin.site.register(Bd, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(Technology, TechnologyAdmin)

