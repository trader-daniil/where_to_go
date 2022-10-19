# Generated by Django 4.1.2 on 2022-10-19 10:04

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_remove_place_name of constraint_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='place',
            name='title and latitude',
        ),
        migrations.RemoveConstraint(
            model_name='place',
            name='title and longitude',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Развернутое описание места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание места'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название места'),
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(fields=('title', 'lat', 'lng'), name='title and latitude'),
        ),
    ]