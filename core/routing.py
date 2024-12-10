from django.urls import path
from core.consumers import DataSyncConsumer

websocket_urlpatterns = [
    path('ws/', DataSyncConsumer.as_asgi()),
]
