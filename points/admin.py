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
    fields = ('name', 'description', 'about_title', 'about_b1',
              'about_b2', 'about_b3', 'about_1', 'about_2', 'about_3',
              'details_title', 'details_b1', 'details_b2', 'details_b3',
              'details_1', 'details_2', 'details_3',
              'we_can', 'we_can_1_title', 'we_can_1', 'we_can_2_title',
              'we_can_2', 'we_can_3_title', 'we_can_3', 'we_can_4_title', 'we_can_4',
              'impl_header', 'impl_title_1', 'impl_ext_1', 'impl_title_2', 'impl_ext_2',
              'impl_title_3', 'impl_ext_3', 'impl_title_4', 'impl_ext_4', 'impl_title_5',
              'impl_ext_5')

admin.site.register(Art_diving, Art_divingAdmin)


class Naive_questionsAdmin(TranslationAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name', 'description', 'about_title', 'about_1', 'about_2',
              'details_title', 'details_1',
              'we_can', 'we_can_1_title', 'we_can_1', 'we_can_2_title',
              'we_can_2', 'we_can_3_title', 'we_can_3', 'impl_header',
              'impl_title_1', 'impl_ext_1', 'impl_title_2', 'impl_ext_2',
              'impl_title_3', 'impl_ext_3')

admin.site.register(Naive_questions, Naive_questionsAdmin)


class Art_cartelAdmin(TranslationAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    fields = ('name', 'description_1', 'description_2',
              'about_title', 'about_1', 'about_2',
              'details_title', 'details_1', 'details_2', 'details_3', 'details_4',
              'impl_header', 'impl_title', 'impl_1', 'impl_2', 'impl_3')

admin.site.register(Art_cartel, Art_cartelAdmin)