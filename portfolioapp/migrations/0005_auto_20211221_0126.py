# Generated by Django 3.2.9 on 2021-12-20 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0004_auto_20211220_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioobject',
            name='square',
            field=models.IntegerField(default=0, verbose_name='Площадь объекта, м2'),
        ),
        migrations.AddField(
            model_name='portfolioobject',
            name='video',
            field=models.TextField(blank=True, max_length=40, verbose_name='Cсылка на видео'),
        ),
        migrations.AlterField(
            model_name='portfolioobject',
            name='object_status',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Завершен ли объект'),
        ),
    ]