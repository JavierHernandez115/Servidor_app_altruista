from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Adulto, Niño, Deseo, Contacto, Necesidad, Dirección, Estudio, Recurso

# Configurar la capa de canales
channel_layer = get_channel_layer()

@receiver(post_save)
def notify_clients(sender, instance, created, **kwargs):
    """
    Señal para notificar a los clientes cuando un modelo relevante es creado o actualizado.
    """
    if sender in [Adulto, Niño, Deseo, Contacto, Necesidad, Dirección, Estudio, Recurso]:
        # Confirmar que la señal se activó correctamente
        if created:
            print(f"Nuevo registro creado en modelo: {sender.__name__}, instancia ID: {instance.id}")
        else:
            print(f"Registro actualizado en modelo: {sender.__name__}, instancia ID: {instance.id}")
        
        # Enviar los datos a través de WebSocket
        async_to_sync(channel_layer.group_send)(
            "sync_group",  # Grupo de WebSocket
            {
                "type": "update_data",  # Tipo de evento manejado por WebSocket
                "data": {
                    "model": sender.__name__,  # Nombre del modelo
                    "instance": instance.id,  # ID de la instancia
                    "created": created,  # Indica si fue creado o actualizado
                },
            }
        )
