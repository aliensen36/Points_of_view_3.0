from django.db import models

class Team(models.Model):
    photo = models.ImageField(upload_to='team', verbose_name='Фото')
    # photo = models.ImageField(upload_to='team_photos/', verbose_name='Фото')
    name = models.CharField(max_length=200, verbose_name='Имя')
    role = models.CharField(max_length=1000, verbose_name='Роль в команде')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Члены команды'
        verbose_name = 'Команда'
        ordering = ['name']