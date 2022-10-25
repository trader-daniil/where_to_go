from adminsortable2.admin import (SortableAdminBase, SortableAdminMixin,
                                  SortableTabularInline)
from django.contrib import admin

from .admin_functions import show_image
from .models import Image, Place


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
