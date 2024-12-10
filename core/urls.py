from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    AdultoViewSet, NiñoViewSet, DeseoViewSet, ContactoViewSet, NecesidadViewSet,
    DirecciónViewSet, EstudioViewSet, RecursoViewSet
)
# Creamos el router para las vistas basadas en ViewSet
router = DefaultRouter()
router.register(r'adultos', AdultoViewSet, basename='adulto')
router.register(r'ninos', NiñoViewSet, basename='nino')
router.register(r'deseos', DeseoViewSet, basename='deseo')
router.register(r'contactos', ContactoViewSet, basename='contacto')
router.register(r'necesidades', NecesidadViewSet, basename='necesidad')
router.register(r'direcciones', DirecciónViewSet, basename='direccion')
router.register(r'estudios', EstudioViewSet, basename='estudio')
router.register(r'recursos', RecursoViewSet, basename='recurso')

urlpatterns = [
    # Rutas REST
    path('', include(router.urls)),
]
