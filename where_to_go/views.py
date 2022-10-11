from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse


def serialize_place(place):
    """
    Сериализует объект локации для шаблона.
    """
    return {
        "place_id": place.id,
        "title": place.title,
        "imgs": [place_photo.image.url for place_photo in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "conditions": {
            "lat": place.lat,
            "lng": place.lng
        },
    }


def show_places(request):
    """
    Возвращает главную страницу со всеми локациями на карте.
    """
    first_place = Place.objects.prefetch_related('images').first()
    second_place = Place.objects.prefetch_related('images').last()
    first_place_serialized = serialize_place(place=first_place)
    second_place_serialized = serialize_place(place=second_place)
    return render(
        request=request,
        template_name='index.html',
        context={
            'first_place': first_place_serialized,
            'second_place': second_place_serialized,
        },
    )


def show_place(request, place_id):
    """
    Возвращает страницу с местом по переданному id.
    """
    place = Place.objects.get(id=place_id)
    serialized_place = serialize_place(place=place)
    return JsonResponse(
        data=serialized_place,
        safe=False,
        json_dumps_params={'ensure_ascii': False},
    )
