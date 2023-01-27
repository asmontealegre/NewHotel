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
    nombreHabitacion = models.CharField(max_length=45, choices=NombreHabitacion.choices, verbose_name="Nombre de Habitación", null=True)
    capacidad = models.CharField(max_length=45, verbose_name="Capacidad")
    cantidad = models.PositiveIntegerField('Cantidad o Stock', default = 1)
    valor = models.IntegerField(verbose_name="Valor")
    descripcion = models.TextField(max_length=200, verbose_name="Descripción")
    class Estado(models.TextChoices):
        ACTIVO = '1', ('Activo')
        INACTIVO = '0', ('Inactivo')
    estado = models.CharField( max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    def __str__(self):
        return "TipoHabitación %s" % (self.nombreHabitacion)

    class Meta:
        verbose_name = 'TipoHabitacion'
        verbose_name_plural = 'TipoHabitaciones'
        ordering = ['nombreHabitacion']


# Habitacion.
class Habitacion(models.Model):
    id = models.AutoField(primary_key = True)
    class Sede(models.TextChoices):
        ESTACION = 'estacion', ('La Estación')
        BOSQUE = 'bosque', ('El Bosque')
    sede = models.CharField(max_length=8, choices=Sede.choices,  verbose_name="Sede", null= True)
    numeroHabitacion = models.IntegerField( verbose_name="Numero de Habitacion")
    class Disponibilidad(models.TextChoices):
        DISPONIBLE = 'Disponible',('Disponible')
        OCUPADA = 'Ocupada',('Ocupada')
    disponibilidad = models.CharField(max_length=10, choices=Disponibilidad.choices,default=Disponibilidad.DISPONIBLE, verbose_name="Disponibilidad")
    class Estado(models.TextChoices):
        ACTIVO = '1', ('Activo')
        INACTIVO = '0', ('Inactivo')
    estado = models.CharField( max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    TipoHabitacion_id = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, verbose_name="Tipo de Habitación",null=True)

    def __str__(self):
        return "Habitación %s" % (self.numeroHabitacion)

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ['numeroHabitacion']