# Generated by Django 3.2.9 on 2021-12-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0008_alter_portfolioobject_main_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioobject',
            name='main_photo',
            field=models.ImageField(blank=True, null=True, upload_to='object_photos/', verbose_name='Главное фото'),
        ),
    ]
