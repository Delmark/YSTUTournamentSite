from django import forms
from django.forms import inlineformset_factory
from .models import News, ArticleImage

class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_desc', 'content', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thumbnail'].required = False

class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False


ArticleImageFormset = inlineformset_factory(
    News,
    ArticleImage,
    form=ArticleImageForm,
    extra=1,
    max_num=10,
    can_delete=True,
    can_order=True,
    labels={'image': 'Изображения:'}
)