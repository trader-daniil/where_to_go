from django.contrib import admin
from .views import show_places, show_place
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', show_places),
    path('admin/', admin.site.urls),
    path('places/<int:place_id>', show_place, name='specific_place'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
