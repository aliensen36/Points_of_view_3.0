from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'role')
    list_display_links = ('name', 'role')
    search_fields = ('name', 'role',)
    fields = ('name', 'role')

admin.site.register(Team, TeamAdmin)

