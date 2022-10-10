from django.db import models

class Place(models.Model):
    """
    Модель достопримечательности.
    """
    title = models.CharField(
        max_length=30,
        verbose_name='Название места',
    )
    description_short = models.TextField(
        verbose_name='Краткое описание места',
    )
    description_long = models.TextField(
        verbose_name='Развернутое описание места',
    )
    lat = models.FloatField(verbose_name='Широта в местоположении')
    lng = models.FloatField(verbose_name='Долгота в местоположении')
