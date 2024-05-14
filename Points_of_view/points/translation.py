from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'role')


@register(Art_diving)
class Art_divingtTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'about_title', 'about_1', 'about_2', 'about_3',
              'details_title', 'details_1', 'details_2', 'details_3')

