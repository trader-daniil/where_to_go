import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from places.models import Image, Place


def get_image(image_url, image_name):
    """Создает объект изображения."""
    response = requests.get(url=image_url)
    response.raise_for_status()

    return ContentFile(
        content=response.content,
        name=image_name,
    )


def parse_place_characteristics(file_url):
    """Получение характеристик достопримечательности из ответа."""
    response = requests.get(url=file_url)
    response.raise_for_status()
    return response.json()


class Command(BaseCommand):
    """Создает объект Place со значением полей из json файла."""

    help = 'Creates Place fields from json file'

    def handle(self, *args, **options):
        file_url = options['file_url']
        place_data = parse_place_characteristics(file_url=file_url)
        try:
            created_place, _ = Place.objects.get_or_create(
                title=place_data['title'],
                lat=float(place_data['coordinates']['lat']),
                lng=float(place_data['coordinates']['lng']),
                defaults={
                    'description_short': place_data.get(
                        'description_short',
                        '',
                    ),
                    'description_long': place_data.get(
                        'description_long',
                        '',
                    ),
                },
            )
        except IntegrityError:
            return 'Проверьте заполненность полей title, lat, lng'

        for image_pos, image_url in enumerate(place_data['imgs'], start=1):
            image_name = f'{created_place.title}{image_pos}.jpg'
            image = get_image(
                image_url=image_url,
                image_name=image_name,
            )
            Image.objects.create(
                place=created_place,
                image=image,
                position=image_pos,
            )

    def add_arguments(self, parser):
        parser.add_argument(
            'file_url',
            action='store',
            type=str,
            help='Указывает путь к файлу, который нужно скачать',
        )
