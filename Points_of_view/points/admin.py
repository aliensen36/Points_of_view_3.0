from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from modeltranslation.admin import TranslationAdmin


class TeamAdmin(TranslationAdmin):
    list_display = ('preview', 'name', 'role')
    list_display_links = ('preview', 'name', 'role')
    search_fields = ('name', 'role',)
    fields = ('name', 'photo', 'preview', 'role')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:150px;">')

admin.site.register(Team, TeamAdmin)



class ProjectAdmin(TranslationAdmin):
    list_display = ('preview', 'name', 'description')
    list_display_links = ('preview', 'name', 'description')
    search_fields = ('name', 'description',)
    fields = ('name', 'photo', 'preview', 'description')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:150px;">')

admin.site.register(Project, ProjectAdmin)