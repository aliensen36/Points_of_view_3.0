# Generated by Django 5.0.4 on 2024-04-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.TextField(verbose_name='Роль в команде'),
        ),
    ]
