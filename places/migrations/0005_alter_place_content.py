# Generated by Django 4.1.2 on 2022-10-13 15:04

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placeimage_options_place_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
