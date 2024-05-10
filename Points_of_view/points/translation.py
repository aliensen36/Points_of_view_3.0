from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'role')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')