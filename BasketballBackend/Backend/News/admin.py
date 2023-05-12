from django.contrib import admin
from .models import News, Photo

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'short_desc', 'content')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_desc', 'content')
        }),
        ('Изображение', {
            'fields': ('thumbnail',)
        }),
        ('Дата публикации', {
            'fields': ('pub_date',)
        }),
    )

admin.site.register(News, NewsAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)

admin.site.register(Photo, PhotoAdmin)