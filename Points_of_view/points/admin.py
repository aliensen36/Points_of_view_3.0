from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from modeltranslation.admin import TranslationAdmin


class TeamAdmin(TranslationAdmin):
    list_display = ('preview', 'name', 'role')
    list_display_links = ('preview', 'name', 'role')
    search_fields = ('name', 'role',)
    fields = ('user_number', 'name', 'photo', 'preview', 'role')
    readonly_fields = ["preview"]
    ordering = ('user_number',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:150px;">')

admin.site.register(Team, TeamAdmin)


class Art_divingAdmin(TranslationAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name', 'description', 'about_title', 'about_1', 'about_2', 'about_3',
              'details_title', 'details_1', 'details_2', 'details_3')

admin.site.register(Art_diving, Art_divingAdmin)
