from django.db import models
from django.core.validators import FileExtensionValidator

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    short_desc = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    thumbnail = models.ImageField(verbose_name='Превью поста', blank=True, upload_to='/news_thumbnails/images/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

    @property
    def get_thumbnail(self):
        if not self.thumbnail:
            return 'media/images/placeholder.png'
        return self.thumbnail

    def __str__(self) -> str:
        return self.title