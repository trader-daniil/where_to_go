
from django.contrib import admin
import traceback

from django.utils.safestring import mark_safe
from .models import Place, PlaceImage


class ImageInstance(admin.TabularInline):
    model = PlaceImage
    
    readonly_fields = ('show_image',)

    def show_image(self, obj):
        width = 200 * (obj.image.width/obj.image.height)
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="{width}" height=200 />')
        except Exception:
            print(traceback.format_exc())


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
    inlines = (ImageInstance,)


@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    list_display = ('get_place_image',)
    """
    readonly_fields = ('show_image',)
    
    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="{obj.image.width}" height={obj.image.height} />')
    """

    @admin.display(ordering='-id')
    def get_place_image(self, obj):
        return f'{obj.id} {obj.place.title}'
