from django.core.management.base import BaseCommand

import requests

from places.models import Place, PlaceImage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    """
    Создает объект Place со значением полей из json файла.
    """
    help = 'Creates Place fields from json file'

    def handle(self, *args, **options):
        file_url = options['fileurl']
        response = requests.get(url=file_url)
        response.raise_for_status()
        place_characteristics = response.json()
        created_place, _ = Place.objects.get_or_create(
            title=place_characteristics['title'],
            description_short=place_characteristics['description_short'],
            description_long=place_characteristics['description_long'],
            lat=float(place_characteristics['coordinates']['lat']),
            lng=float(place_characteristics['coordinates']['lng']),
        )

        for image_pos, image_url in enumerate(
            place_characteristics['imgs'],
            start=1):
            response = requests.get(url=image_url)
            response.raise_for_status()
            image = ContentFile(response.content)
            created_imageplace, _ = PlaceImage.objects.get_or_create(
                place=created_place,
                position=image_pos,
            )
            created_imageplace.image.save(
                name=f'{created_place.title}{image_pos}.jpg',
                content=image,
                save=True,
            )


    def add_arguments(self, parser):
        parser.add_argument(
            'fileurl',
            action='store', 
            type=str,
            help='Указывает путь к файлу, который нужно скачать',
        )
