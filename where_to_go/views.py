from django.shortcuts import render
from places.models import Place
import json


def serialize_place(place):
    return {
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
    places = Place.objects.prefetch_related('images').all()
    serialized_places = [serialize_place(place=place) for place in places]
    return render(
        request=request,
        template_name='index.html',
        context={'places': serialized_places},
    )


def test_serializer(request):
    places = Place.objects.prefetch_related('images').all()
    serialized_places = [serialize_place(place=place) for place in places]
    return render(
        request=request,
        template_name='test.html',
        context={'places': serialized_places}
    )
