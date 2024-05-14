from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'role')


@register(Art_diving)
class Art_divingtTranslationOptions(TranslationOptions):
    fields = ('name', 'description',
              'about_title', 'about_b1', 'about_b2', 'about_b3',
              'about_1', 'about_2', 'about_3',
              'details_title', 'details_b1', 'details_b2', 'details_b3',
              'details_1', 'details_2', 'details_3',
              'we_can', 'we_can_1_title', 'we_can_1', 'we_can_2_title',
              'we_can_2', 'we_can_3_title', 'we_can_3', 'we_can_4_title', 'we_can_4',
              'impl_header', 'impl_title_1', 'impl_ext_1', 'impl_title_2', 'impl_ext_2',
              'impl_title_3', 'impl_ext_3', 'impl_title_4', 'impl_ext_4', 'impl_title_5',
              'impl_ext_5')


@register(Naive_questions)
class Naive_questionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',
              'about_title', 'about_1', 'about_2',
              'details_title', 'details_1',
              'we_can', 'we_can_1_title', 'we_can_1', 'we_can_2_title',
              'we_can_2', 'we_can_3_title', 'we_can_3', 'impl_header',
              'impl_title_1', 'impl_ext_1', 'impl_title_2', 'impl_ext_2',
              'impl_title_3', 'impl_ext_3')