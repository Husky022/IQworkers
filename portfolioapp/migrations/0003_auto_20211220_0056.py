# Generated by Django 3.2.9 on 2021-12-19 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_portfolioimage_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioimage',
            name='is_main_photo',
            field=models.BooleanField(default=False, verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='portfolioimage',
            name='image',
            field=models.FileField(null=True, upload_to='object_photos/'),
        ),
    ]
