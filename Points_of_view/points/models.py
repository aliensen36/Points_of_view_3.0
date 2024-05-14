from django.db import models

class Team(models.Model):
    photo = models.ImageField(upload_to='team', verbose_name='Фото')
    name = models.CharField(max_length=200, verbose_name='Имя')
    role = models.TextField(verbose_name='Роль в команде')
    user_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Члены команды'
        verbose_name = 'Команда'
        ordering = ['user_number']


class Art_diving(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    about_title = models.TextField(verbose_name='О проекте(заголовок)')
    about_b1 = models.TextField(verbose_name='О проекте(бл. 1)')
    about_b2 = models.TextField(verbose_name='О проекте(бл. 2)')
    about_b3 = models.TextField(verbose_name='О проекте(бл. 3)')
    about_1 = models.TextField(verbose_name='О проекте(абз. 1)')
    about_2 = models.TextField(verbose_name='О проекте(абз. 2)')
    about_3 = models.TextField(verbose_name='О проекте(абз. 3)')
    details_title = models.TextField(verbose_name='Детали(заголовок)')
    details_b1 = models.TextField(verbose_name='Детали(бл. 1)')
    details_b2 = models.TextField(verbose_name='Детали(бл. 2)')
    details_b3 = models.TextField(verbose_name='Детали(бл. 3)')
    details_1 = models.TextField(verbose_name='Детали(абз. 1)')
    details_2 = models.TextField(verbose_name='Детали(абз. 2)')
    details_3 = models.TextField(verbose_name='Детали(абз. 3)')
    we_can = models.TextField(verbose_name='Умеем')
    we_can_1_title = models.TextField(verbose_name='Умеем_1(заг.)')
    we_can_1 = models.TextField(verbose_name='Умеем_1')
    we_can_2_title = models.TextField(verbose_name='Умеем_2(заг.)')
    we_can_2 = models.TextField(verbose_name='Умеем_2')
    we_can_3_title = models.TextField(verbose_name='Умеем_3(заг.)')
    we_can_3 = models.TextField(verbose_name='Умеем_3')
    we_can_4_title = models.TextField(verbose_name='Умеем_4(заг.)')
    we_can_4 = models.TextField(verbose_name='Умеем_4')
    impl_header = models.TextField(verbose_name='Реализация')
    impl_title_1 = models.TextField(verbose_name='Реализация(заг.1)')
    impl_ext_1 = models.TextField(verbose_name='Реализация(инф.1)')
    impl_title_2 = models.TextField(verbose_name='Реализация(заг.2)')
    impl_ext_2 = models.TextField(verbose_name='Реализация(инф.2)')
    impl_title_3 = models.TextField(verbose_name='Реализация(заг.3)')
    impl_ext_3 = models.TextField(verbose_name='Реализация(инф.3)')
    impl_title_4 = models.TextField(verbose_name='Реализация(заг.4)')
    impl_ext_4 = models.TextField(verbose_name='Реализация(инф.4)')
    impl_title_5 = models.TextField(verbose_name='Реализация(заг.5)')
    impl_ext_5 = models.TextField(verbose_name='Реализация(инф.5)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Арт-дивинг'
        verbose_name = 'Арт-дивинг'


class Naive_questions(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    about_title = models.TextField(verbose_name='О проекте(заголовок)')
    about_1 = models.TextField(verbose_name='О проекте(абз. 1)')
    about_2 = models.TextField(verbose_name='О проекте(абз. 2)')
    details_title = models.TextField(verbose_name='Детали(заголовок)')
    details_1 = models.TextField(verbose_name='Детали(абз. 1)')
    we_can = models.TextField(verbose_name='Умеем')
    we_can_1_title = models.TextField(verbose_name='Умеем_1(заг.)')
    we_can_1 = models.TextField(verbose_name='Умеем_1')
    we_can_2_title = models.TextField(verbose_name='Умеем_2(заг.)')
    we_can_2 = models.TextField(verbose_name='Умеем_2')
    we_can_3_title = models.TextField(verbose_name='Умеем_3(заг.)')
    we_can_3 = models.TextField(verbose_name='Умеем_3')
    impl_header = models.TextField(verbose_name='Реализация')
    impl_title_1 = models.TextField(verbose_name='Реализация(заг.1)')
    impl_ext_1 = models.TextField(verbose_name='Реализация(инф.1)')
    impl_title_2 = models.TextField(verbose_name='Реализация(заг.2)')
    impl_ext_2 = models.TextField(verbose_name='Реализация(инф.2)')
    impl_title_3 = models.TextField(verbose_name='Реализация(заг.3)')
    impl_ext_3 = models.TextField(verbose_name='Реализация(инф.3)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Наивные вопросы'
        verbose_name = 'Наивные вопросы'