from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Adulto, Niño, Deseo, Contacto, Necesidad, Dirección, Estudio, Recurso
from core.serializers import (
    AdultoSerializer, NiñoSerializer, DeseoSerializer, ContactoSerializer,
    NecesidadSerializer, DirecciónSerializer, EstudioSerializer, RecursoSerializer
)

class AdultoViewSet(ModelViewSet):
    queryset = Adulto.objects.all()
    serializer_class = AdultoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nombres', 'fecha_registro']  # Filtros exactos
    search_fields = ['nombres', 'apellido_paterno', 'apellido_materno']  # Búsqueda parcial
    ordering_fields = ['fecha_registro', 'edad']  # Ordenar por estos campos
    ordering = ['nombres']  # Orden predeterminado


class NiñoViewSet(ModelViewSet):
    queryset = Niño.objects.all()
    serializer_class = NiñoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['edad', 'padres__nombres']
    search_fields = ['nombres', 'apellido_paterno', 'padres__nombres']
    ordering_fields = ['edad', 'nombres']
    ordering = ['nombres']


class DeseoViewSet(ModelViewSet):
    queryset = Deseo.objects.all()
    serializer_class = DeseoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['niño__nombres', 'fecha']
    search_fields = ['deseo', 'niño__nombres']
    ordering_fields = ['fecha']
    ordering = ['fecha']


class ContactoViewSet(ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['numero', 'dueño__nombres']


class NecesidadViewSet(ModelViewSet):
    queryset = Necesidad.objects.all()
    serializer_class = NecesidadSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['solicitante__nombres', 'fecha_solicitada']
    search_fields = ['necesidad', 'solicitante__nombres']
    ordering_fields = ['fecha_solicitada']
    ordering = ['fecha_solicitada']


class DirecciónViewSet(ModelViewSet):
    queryset = Dirección.objects.all()
    serializer_class = DirecciónSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dueño__nombres', 'estado', 'municipio']
    search_fields = ['calle', 'colonia', 'dueño__nombres']
    ordering_fields = ['estado', 'municipio']
    ordering = ['estado']


class EstudioViewSet(ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['padre__nombres', 'num_habitantes', 'trabajadores']
    search_fields = ['vivienda', 'techo', 'padre__nombres']
    ordering_fields = ['num_habitantes', 'trabajadores']
    ordering = ['num_habitantes']


class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dador__nombres', 'unidad']
    search_fields = ['descripcion', 'dador__nombres']
    ordering_fields = ['cantidad']
    ordering = ['cantidad']
