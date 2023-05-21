from django.contrib import admin
from .models import News, ArticleImage, Photo, Partner

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['title', 'short_desc', 'content']
    readonly_fields = ('pub_date',)  # добавить pub_date сюда
    fieldsets = (
        (None, {
            'fields': ['title', 'short_desc', 'content', 'thumbnail']
        }),
    )
    inlines = [ArticleImageInline]

admin.site.register(News, NewsAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['pub_date']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Partner)