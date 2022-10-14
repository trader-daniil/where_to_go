
from django.contrib import admin
import traceback

from django.utils.safestring import mark_safe
from .models import Place, PlaceImage

from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase

from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.db.models import TextField


class ImageInstance(SortableTabularInline):
    model = PlaceImage
    
    readonly_fields = ('show_image',)
    ordering = ['position']

    def show_image(self, obj):
        width = 200 * (obj.image.width/obj.image.height)
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="{width}" height=200 />')
        except Exception:
            print(traceback.format_exc())


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
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
    """
    formfield_overrides = {
        HTMLField: {'widget': TinyMCE()},
    }
    """


@admin.register(PlaceImage)
class AdminPlaceImage(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['position']
    readonly_fields = ('show_image',)

    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="{obj.image.width}" height={obj.image.height} />')
