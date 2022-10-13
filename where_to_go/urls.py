from django.contrib import admin
from .views import show_places, show_place, test_data
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', show_places),
    path('admin/', admin.site.urls),
    path('test/', test_data),
    path('places/<int:place_id>', show_place, name='current_place')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
