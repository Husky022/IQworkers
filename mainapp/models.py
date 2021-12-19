from django.db import models


# Create your models here.

class PortfolioObject(models.Model):
    class Meta:
        ordering = ['-id']

    name = models.CharField(verbose_name='Название объекта', max_length=168)
    preview = models.TextField(verbose_name='Предпросмотр', max_length=250)
    text = models.TextField(verbose_name='Текст по объекту')
    is_active = models.BooleanField(verbose_name='Актуальность объекта', default=True, db_index=True)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='Начало работы по объекту')
    finish_date = models.DateTimeField(verbose_name='Конец работы по объекту')
    object_status = models.TextField(verbose_name='Предпросмотр', max_length=20, default='В работе')


class PortfolioImage(models.Model):
    pass


class PortfolioFunctions(models.Model):
    pass

