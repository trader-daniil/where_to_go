import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from places.models import Image, Place


def create_place(place_url):
    """Скачивает данные о месте и возвращает его."""
    response = requests.get(url=place_url)
    response.raise_for_status()
    place_data = response.json()
    return Place.objects.get_or_create(
        title=place_data['title'],
        lat=place_data['coordinates']['lat'],
        lng=place_data['coordinates']['lng'],
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


def create_image(place, image_url, image_pos):
    """Сохраняет изображение и связывает его с местом."""
    image_name = f'{place.title}{image_pos}.jpg'
    place_images = place.images.all()
    response = requests.get(url=image_url)
    response.raise_for_status()
    image = ContentFile(
        content=response.content,
        name=image_name,
    )
    for place_image in place_images:
        with open(place_image.image.path, 'rb') as current_image:
            if current_image.read() == response.content:
                return None
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

        try:
            place, created = create_place(place_url=file_url)
        except IntegrityError:
            return 'Проверьте заполненность полей title, lat, lng'
        if not created:
            return 'Место было создано ранее'
        response = requests.get(url=file_url)
        response.raise_for_status()
        image_urls = response.json()['imgs']
        for image_pos, image_url in enumerate(image_urls, start=1):
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
