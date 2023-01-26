from django.db import models

# Create your models here.
# Tipo Habitacion.
class TipoHabitacion(models.Model):
    class NombreHabitacion(models.TextChoices):
        SENCILLA = 'Sencilla', ('Sencilla')
        DOBLE = 'Doble', ('Doble')
        CAMPESTRE = 'Campestre', ('Campestre')
        INDIVIDUAL = 'Individual', ('Individual')
        DOBLEKING = 'Doble King', ('Doble King')
        ALPINA = 'Cabaña Alpina', ('Cabaña Alpina')     
    nombreHabitacion = models.CharField(max_length=45, choices=NombreHabitacion.choices, verbose_name="Nombre Habitacion", null=True)
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion Habitacion")
    capacidad = models.CharField(max_length=45, verbose_name="Capacidad")
    valor = models.IntegerField(verbose_name="Valor Habitacion")
    class Sede(models.TextChoices):
        ESTACION = 'estacion', ('La Estación')
        BOSQUE = 'bosque', ('El Bosque')
    sede = models.CharField(max_length=8, choices=Sede.choices, default=Sede.ESTACION, verbose_name="Sede")
    cantidad = models.PositiveIntegerField('Cantidad o Stock', default = 1)
    class Estado(models.TextChoices):
        ACTIVO = '1', ('Activo')
        INACTIVO = '0', ('Inactivo')
    estado = models.CharField( max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s " % (self.nombreHabitacion)


# Habitacion.
class Habitacion(models.Model):
    id = models.AutoField(primary_key = True)
    
    numeroHabitacion = models.IntegerField( verbose_name="Numero de Habitacion")
    class Disponibilidad(models.TextChoices):
        DISPONIBLE = 'Disponible',('Disponible')
        OCUPADA = 'Ocupada',('Ocupada')
    disponibilidad = models.CharField(max_length=10, choices=Disponibilidad.choices,default=Disponibilidad.DISPONIBLE, verbose_name="Disponibilidad")
    class Estado(models.TextChoices):
        ACTIVO = '1', ('Activo')
        INACTIVO = '0', ('Inactivo')
    estado = models.BooleanField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "Habitación %s" % (self.numeroHabitacion)