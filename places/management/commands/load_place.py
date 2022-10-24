from django.core.management.base import BaseCommand

import requests

from places.models import Place, Image
from django.core.files.base import ContentFile


def get_image(image_url):
    """Создает объект изображения."""
    response = requests.get(url=image_url)
    response.raise_for_status()
    return ContentFile(response.content)


def parse_place_characteristics(file_url):
    """Получение характеристик достопримечательности из ответа."""
    response = requests.get(url=file_url)
    response.raise_for_status()
    return response.json()


def create_image(place, image_pos, image):
    """Связывает сзображение с объектом PlaceImage."""
    created_image_place, _ = Image.objects.get_or_create(
        place=place,
        position=image_pos,
    )
    created_image_place.image.save(
        name=f'{place.title}{image_pos}.jpg',
        content=image,
        save=True,
    )


class Command(BaseCommand):
    """Создает объект Place со значением полей из json файла."""

    help = 'Creates Place fields from json file'

    def handle(self, *args, **options):
        file_url = options['file_url']
        place_data = parse_place_characteristics(file_url=file_url)
        created_place, _ = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            lat=float(place_data['coordinates']['lat']),
            lng=float(place_data['coordinates']['lng']),
        )

        for image_pos, image_url in enumerate(
            place_data['imgs'],
            start=1,
        ):
            image = get_image(image_url=image_url)
            create_image(
                place=created_place,
                image_pos=image_pos,
                image=image,
            )

    def add_arguments(self, parser):
        parser.add_argument(
            'file_url',
            action='store',
            type=str,
            help='Указывает путь к файлу, который нужно скачать',
        )
