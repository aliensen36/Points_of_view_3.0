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
    about_1 = models.TextField(verbose_name='О проекте(абз. 1)')
    about_2 = models.TextField(verbose_name='О проекте(абз. 2)')
    about_3 = models.TextField(verbose_name='О проекте(абз. 3)')
    details_title = models.TextField(verbose_name='Детали(заголовок)')
    details_1 = models.TextField(verbose_name='Детали(абз. 1)')
    details_2 = models.TextField(verbose_name='Детали(абз. 2)')
    details_3 = models.TextField(verbose_name='Детали(абз. 3)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Арт-дивинг'
        verbose_name = 'Арт-дивинг'