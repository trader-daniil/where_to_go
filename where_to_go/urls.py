from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import show_map_with_places, show_place

urlpatterns = [
    path('', show_map_with_places),
    path('admin/', admin.site.urls),
    path('places/<int:place_id>', show_place, name='specific_place'),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
