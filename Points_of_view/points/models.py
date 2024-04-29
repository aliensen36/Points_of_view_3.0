from django.db import models

class Team(models.Model):
    photo = models.ImageField(verbose_name='Фото')
    # photo = models.ImageField(upload_to='team_photos/', verbose_name='Фото')
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
