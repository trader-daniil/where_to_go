from django.contrib import admin
from .views import show_places
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', show_places),
    path('admin/', admin.site.urls),
    #path('test/', test_serializer),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
