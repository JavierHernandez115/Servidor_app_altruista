import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils.timezone import now
from datetime import timedelta, date

class DataSyncConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "sync_group"  # Asignación del grupo

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

        # Cargar datos iniciales (por defecto del último mes)
        self.send_data_for_range('mes')

    def disconnect(self, close_code):
        if hasattr(self, 'group_name'):  # Comprobamos que group_name está definido
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name
            )
        self.close()  # Asegúrate de cerrar la conexión correctamente

    class DateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            return super().default(obj)

    def send_data_for_range(self, range_type):
        from .models import Adulto, Niño, Deseo, Contacto, Necesidad, Dirección, Estudio, Recurso

        now_date = now()
        if range_type == 'ultimo_dia':
            start_date = now_date - timedelta(days=1)
        elif range_type == 'semana':
            start_date = now_date - timedelta(weeks=1)
        elif range_type == 'mes':
            start_date = now_date - timedelta(days=30)
        elif range_type == 'bimestre':
            start_date = now_date - timedelta(days=60)
        elif range_type == 'semestre':
            start_date = now_date - timedelta(days=180)
        elif range_type == 'anio':
            start_date = now_date - timedelta(days=365)
        else:
            start_date = now_date - timedelta(days=30)  # Rango por defecto: último mes

        # Filtrar los objetos basados en el rango de fechas
        adultos = list(Adulto.objects.filter(fecha_registro__gte=start_date).values())
        niños = list(Niño.objects.filter(padres__fecha_registro__gte=start_date).values())
        deseos = list(Deseo.objects.filter(fecha__gte=start_date).values())
        contactos = list(Contacto.objects.filter(dueño__fecha_registro__gte=start_date).values())
        necesidades = list(Necesidad.objects.filter(fecha_solicitada__gte=start_date).values())
        direcciones = list(Dirección.objects.filter(dueño__fecha_registro__gte=start_date).values())
        estudios = list(Estudio.objects.filter(padre__fecha_registro__gte=start_date).values())
        recursos = list(Recurso.objects.all().values())

        # Haz lo mismo para otros modelos si es necesario...

        data = {
            "range": range_type,
            "adultos": adultos,
            "niños": niños,
            "deseos": deseos,
            "contactos": contactos,
            "necesidades": necesidades,
            "direcciones": direcciones,
            "estudios": estudios,
            "recursos": recursos,
        }

        self.send(text_data=json.dumps(data, cls=self.DateEncoder))

    def receive(self, text_data):
        """
        Manejar mensajes del cliente, como la solicitud de un rango de tiempo diferente.
        """
        request = json.loads(text_data)
        range_type = request.get('range', 'mes')  # Por defecto: último mes
        self.send_data_for_range(range_type)

    def update_data(self, event):
        """
        Enviar actualizaciones incrementales al cliente.
        """
        self.send(text_data=json.dumps({
            "type": "update",
            "data": event["data"]
        }))
