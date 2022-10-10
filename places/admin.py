from django.contrib import admin

from .models import Place


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
