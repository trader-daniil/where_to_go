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
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        },
        "url_addres": place.get_absolute_url(),
    }


def show_map_with_places(request):
    """
    Возвращает главную страницу со всеми локациями на карте.
    """
    places = Place.objects.prefetch_related('images').all()
    serialized_places = [serialize_place(place=place) for place in places]
    return render(
        request=request,
        template_name='mainpage.html',
        context={
            'places': serialized_places,
        }
    )


def show_place(request, place_id):
    """
    Возвращает страницу с местом по переданному id.
    """
    place = Place.objects.prefetch_related('images').get(id=place_id)
    serialized_place = serialize_place(place=place)
    return JsonResponse(
        data=serialized_place,
        safe=False,
        json_dumps_params={'ensure_ascii': False},
    )

def test_verbtain(request):
    place = Place.objects.first()
    return render(
        request=request,
        template_name='test.html',
        context={'place': place},
    )