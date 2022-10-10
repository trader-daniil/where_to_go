
from django.contrib import admin

from .models import Place, PlaceImage


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = (
        'title',
        'lat',
        'lng',
    )
    search_fields = (
        'title',
        'description_long',
    )

@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    list_display = ('get_place_image',)

    @admin.display(ordering='-id')
    def get_place_image(self, obj):
        return f'{obj.id} {obj.place.title}'

