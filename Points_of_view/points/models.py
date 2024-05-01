from django.db import models

class Team(models.Model):
    photo = models.ImageField(upload_to='team', verbose_name='Фото')
    name = models.CharField(max_length=200, verbose_name='Имя')
    role = models.TextField(verbose_name='Роль в команде')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Члены команды'
        verbose_name = 'Команда'
        ordering = ['name']


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='project', verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['name']
