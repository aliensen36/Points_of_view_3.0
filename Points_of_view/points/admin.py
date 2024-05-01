from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name', 'role')
    list_display_links = ('preview', 'name', 'role')
    search_fields = ('name', 'role',)
    fields = ('name', 'photo', 'preview', 'role')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:150px;">')


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['role'].widget.attrs['style'] = ('width: auto; '
                                                          'min-width: 200px; '
                                                          'min-height: 50px; '
                                                          'resize: both; '
                                                          'overflow: auto; '
                                                          'word-wrap: break-word; '
                                                          'overflow-wrap: break-word;')
        return form

    # class Media:
    #     css = {
    #         'all': ('admin/textarea-autosize.css',),
    #     }


admin.site.register(Team, TeamAdmin)



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name', 'description')
    list_display_links = ('preview', 'name', 'description')
    search_fields = ('name', 'description',)
    fields = ('name', 'photo', 'preview', 'description')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:150px;">')


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['style'] = ('width: auto; '
                                                          'min-width: 200px; '
                                                          'min-height: 50px; '
                                                          'resize: both; '
                                                          'overflow: auto; '
                                                          'word-wrap: break-word; '
                                                          'overflow-wrap: break-word;')
        return form

    # class Media:
    #     css = {
    #         'all': ('admin/textarea-autosize.css',),
    #     }


admin.site.register(Project, ProjectAdmin)
