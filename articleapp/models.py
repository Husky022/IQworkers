from django.db import models

# Create your models here.

class Article(models.Model):
    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['-add_datetime']

    name = models.CharField(verbose_name='Название статьи', max_length=168)
    main_image = models.ImageField(verbose_name='Изображение для статьи', blank=True, upload_to='article_photos/')
    preview = models.TextField(verbose_name='Предпросмотр', max_length=250)
    text = models.TextField(verbose_name='Текст статьи')

    is_active = models.BooleanField(verbose_name='Актуальность статьи', default=True, db_index=True)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
