# Generated by Django 4.2 on 2023-05-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0006_remove_teamstatistic_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstatistic',
            name='logo',
            field=models.ImageField(blank=True, upload_to='teams/logos/', verbose_name='Логотип команды'),
        ),
        migrations.AlterField(
            model_name='teamstatistic',
            name='rating',
            field=models.IntegerField(blank=True, default=0, verbose_name='Рейтинг команды'),
        ),
    ]
