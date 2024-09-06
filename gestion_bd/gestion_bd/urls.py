# gestion_bd/urls.py (archivo principal de URLs)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('administracion.urls')),
    # Añadir otras rutas si es necesario
]
