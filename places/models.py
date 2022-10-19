from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


class Place(models.Model):
    """
    Модель достопримечательности.
    """
    title = models.CharField(
        max_length=256,
        verbose_name='Название места',
    )
    description_short = models.TextField(
        verbose_name='Краткое описание места',
        blank=True,
    )
    description_long = HTMLField(
        verbose_name='Развернутое описание места',
        blank=True,
    )
    lat = models.FloatField(verbose_name='Широта в местоположении')
    lng = models.FloatField(verbose_name='Долгота в местоположении')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "lat"],
                name='title and latitude',
            ),
            models.UniqueConstraint(
                fields=["title", "lng"],
                name='title and longitude',
            )
        ]

    def get_absolute_url(self):
        return reverse(
            'specific_place',
            kwargs={'place_id': str(self.id)},
        )


class PlaceImage(models.Model):
    """
    Модель изображения для места.
    """
    place = models.ForeignKey(
        Place,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='место на фотографии',
    )
    image = models.ImageField(
        verbose_name='Изображение места',
    )
    position = models.PositiveIntegerField(
        null=True,
        verbose_name='Позиция фото для места'
    )

    class Meta:
        ordering = ['position']
        unique_together = (
            'place',
            'image',
        )

    def __str__(self):
        return f'{self.id} {self.place.title}'
