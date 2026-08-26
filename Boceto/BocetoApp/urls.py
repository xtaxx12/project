from django.urls import path
from django.views.generic.base import RedirectView
from BocetoApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Páginas principales (slugs en minúsculas y con guiones)
    path("", views.home, name="index"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("colaboradores/", views.colaboradores, name="colaboradores"),
    path("labor-social/", views.labor, name="labor"),
    path("bana-pan/", views.banapan, name="banapan"),
    path("cooporoverdesa/", views.cooporoverdesa, name="cooporoverdesa"),

    # Redirects 301 desde las rutas antiguas (SEO / enlaces existentes)
    path("Nosotros/", RedirectView.as_view(pattern_name="nosotros", permanent=True)),
    path("Colaboradores/", RedirectView.as_view(pattern_name="colaboradores", permanent=True)),
    path("Labor_social/", RedirectView.as_view(pattern_name="labor", permanent=True)),
    path("Bana_Pan/", RedirectView.as_view(pattern_name="banapan", permanent=True)),
    path("Cooporoverdesa/", RedirectView.as_view(pattern_name="cooporoverdesa", permanent=True)),

    # Contacto y Cotización
    path("contacto/enviar/", views.enviar_correo, name="enviar_correo"),
    path("cotizacion/", views.cotizacion, name="cotizacion"),
    path("cotizacion/enviar/", views.enviar_cotizacion, name="enviar_cotizacion"),

    # Noticias
    path("noticias/", views.noticias, name="noticias"),
    path("noticia/<int:noticia_id>/", views.ver_noticia, name="ver_noticia"),
]

# Servir archivos multimedia en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
