from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse


def serialize_place(place):
    """Сериализует объект локации для шаблона."""
    return {
        'title': place.title,
        'imgs': [place_photo.image.url for place_photo in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
        },
    }


def show_place(request, place_id):
    """Возвращает страницу с местом по переданному id."""
    place = Place.objects.get(id=place_id)
    serialized_place = serialize_place(place=place)
    return JsonResponse(
        data=serialized_place,
        safe=False,
        json_dumps_params={'ensure_ascii': False},
    )


def serialize_place_for_map(place):
    """Сериализует объект для JS скрипта."""
    serialized_place = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat],
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse(
                'specific_place',
                kwargs={'place_id': place.id},
            ),
        },
    }
    return serialized_place


def show_map_with_places(request):
    """Возвращает главную страницу со всеми локациями на карте."""
    places = Place.objects.all()
    data_for_map = {
        'type': 'FeatureCollection',
        'features': [serialize_place_for_map(place) for place in places],
    }

    return render(
        request=request,
        template_name='mainpage.html',
        context={'data': data_for_map},
    )
