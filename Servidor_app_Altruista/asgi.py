"""
ASGI config for Servidor_app_Altruista project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from core.routing import websocket_urlpatterns  # Asegúrate de que las rutas WebSocket estén configuradas

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Servidor_app_Altruista.settings')

# Configuración de la aplicación ASGI
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Maneja solicitudes HTTP normales
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Rutas de WebSocket importadas desde routing.py
        )
    ),
})
