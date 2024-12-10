from django.db import models

class Adulto(models.Model):
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_adultos/')
    fecha_registro = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"


class Niño(models.Model):
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    padres = models.ForeignKey(Adulto, on_delete=models.CASCADE, related_name='hijos')

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"


class Deseo(models.Model):
    niño = models.ForeignKey(Niño, on_delete=models.CASCADE, related_name='deseos')
    deseo = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"Deseo de {self.niño.nombres}: {self.deseo}"


class Contacto(models.Model):
    numero = models.CharField(max_length=20)
    dueño = models.ForeignKey(Adulto, on_delete=models.CASCADE, related_name='contactos')

    def __str__(self):
        return self.numero


class Necesidad(models.Model):
    necesidad = models.TextField()
    solicitante = models.ForeignKey(Adulto, on_delete=models.CASCADE, related_name='necesidades')
    fecha_solicitada = models.DateField()

    def __str__(self):
        return self.necesidad


class Dirección(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cp = models.CharField(max_length=10)
    referencia = models.TextField()
    dueño = models.ForeignKey(Adulto, on_delete=models.CASCADE, related_name='direcciones')

    def __str__(self):
        return f"{self.calle}, {self.colonia}, {self.municipio}"


class Estudio(models.Model):
    vivienda = models.CharField(max_length=255)
    techo = models.CharField(max_length=255)
    piso = models.CharField(max_length=255)
    combustible_cocina = models.CharField(max_length=255)
    num_habitantes = models.IntegerField()
    trabajadores = models.IntegerField()
    padre = models.ForeignKey(Adulto, on_delete=models.CASCADE, related_name='estudios')

    def __str__(self):
        return f"Estudio de {self.padre.nombres}"


class Recurso(models.Model):
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=50)
    descripcion = models.TextField()
    dador = models.ForeignKey(Adulto, on_delete=models.SET_NULL, null=True, blank=True, related_name='recursos_donados')

    def __str__(self):
        return self.descripcion
