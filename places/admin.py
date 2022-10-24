from django.contrib import admin

from .models import Place, Image

from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminMixin
from adminsortable2.admin import SortableAdminBase

from .admin_functions import show_image


class ImageInstance(SortableTabularInline):
    model = Image
    readonly_fields = ('submitted_images',)
    ordering = ['position']
    submitted_images = show_image


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


@admin.register(Image)
class AdminPlaceImage(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['position']
    readonly_fields = ('submitted_images',)
    submitted_images = show_image
