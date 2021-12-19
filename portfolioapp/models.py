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
    object_status = models.TextField(verbose_name='Статус объекта', max_length=20, default='В работе')
    function_light = models.BooleanField(verbose_name='Функционал: Освещение', default=True)
    function_shutters = models.BooleanField(verbose_name='Функционал: Шторы', default=False)
    function_ventilation = models.BooleanField(verbose_name='Функционал: Вентиляция', default=False)
    function_condition = models.BooleanField(verbose_name='Функционал: Кондиционирование', default=False)
    function_warm_floors = models.BooleanField(verbose_name='Функционал: Теплые полы', default=False)
    function_security = models.BooleanField(verbose_name='Функционал: Безопасность', default=False)
    function_remote = models.BooleanField(verbose_name='Функционал: Удаленное управление', default=False)
    function_voice_control = models.BooleanField(verbose_name='Функционал: Голосовые помощники', default=False)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    object = models.ForeignKey(PortfolioObject, on_delete=models.CASCADE,
                               verbose_name='Объект', related_name='object', null=True, db_index=True)
    image = models.FileField(upload_to='object_photos/', null=True)
    is_active = models.BooleanField(verbose_name='Актуальность фото', default=True, db_index=True)
    is_main_photo = models.BooleanField(verbose_name='Главное фото', default=False)

    def __str__(self):
        return self.image.name
