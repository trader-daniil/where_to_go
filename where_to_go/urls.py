from django.contrib import admin
from .views import show_phones
from django.urls import path

urlpatterns = [
    path('', show_phones),
    path('admin/', admin.site.urls),
]
