from django.db import models
from django.core.validators import FileExtensionValidator

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    short_desc = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    thumbnail = models.ImageField(verbose_name='Превью поста', blank=True, upload_to='news_thumbnails/images/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

    @property
    def get_thumbnail(self):
        if not self.thumbnail:
            return 'media/images/placeholder.png'
        return self.thumbnail.url

    def __str__(self) -> str:
        return self.title
    
class ArticleImage(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.article.title

class Photo(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='gallery/images/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    @property
    def get_image(self):
        if not self.image:
            return 'media/images/placeholder.png'
        return self.image.url

    def __str__(self) -> str:
        return self.title

class Partner(models.Model):
    company_name = models.CharField(verbose_name="Название компании", max_length=120)
    partner_description = models.TextField(verbose_name="Описание партнёра")
    partner_site_link = models.URLField(verbose_name="Ссылка на сайт партнёра", blank=True, null=True)
    photo = models.ImageField(verbose_name='Логотип партнёра', blank=True, upload_to='partners/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])

    def __str__(self):
        return f"О партнёре {self.company_name}"
