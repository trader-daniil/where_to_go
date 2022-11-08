import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from places.models import Image, Place


def create_place(place_data):
    """Скачивает данные о месте и возвращает его."""
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
    return created_place


def create_image(place, image_url, image_pos):
    """Сохраняет изображение и связывает его в местом."""
    image_name = f'{place.title}{image_pos}.jpg'
    response = requests.get(url=image_url)
    response.raise_for_status()
    image = ContentFile(
        content=response.content,
        name=image_name,
    )
    Image.objects.create(
        place=place,
        image=image,
        position=image_pos,
    )


class Command(BaseCommand):
    """Создает объект Place со значением полей из json файла."""

    help = 'Creates Place fields from json file'

    def handle(self, *args, **options):
        file_url = options['file_url']
        response = requests.get(url=file_url)
        response.raise_for_status()
        place_data = response.json()
        try:
            place = create_place(place_data=place_data)
        except IntegrityError:
            return 'Проверьте заполненность полей title, lat, lng'

        for image_pos, image_url in enumerate(place_data['imgs'], start=1):
            create_image(
                place=place,
                image_url=image_url,
                image_pos=image_pos,
            )

    def add_arguments(self, parser):
        parser.add_argument(
            'file_url',
            action='store',
            type=str,
            help='Указывает путь к файлу, который нужно скачать',
        )
