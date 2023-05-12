# Generated by Django 4.2 on 2023-05-12 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='news_thumbnails/images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Превью поста'),
        ),
    ]
