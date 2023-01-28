from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
# PQRS.
class PQRS(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres",blank=True) 
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos",blank=True)
    telefono=models.CharField(max_length=15, verbose_name="Teléfono",blank=True)
    email=models.CharField(max_length=50, verbose_name="Correo Electronico", blank=True)
    class NombreHabitacion(models.TextChoices):
        SENCILLA = 'Sencilla', ('Sencilla')
        DOBLE = 'Doble', ('Doble')
        CAMPESTRE = 'Campestre', ('Campestre')
        INDIVIDUAL = 'Individual', ('Individual')
        DOBLEKING = 'Doble King', ('Doble King')
        ALPINA = 'Cabaña Alpina', ('Cabaña Alpina')     
    asunto=models.CharField(max_length=45, verbose_name="Asunto")
    comentarioCliente=models.CharField(max_length=250, verbose_name="Comentario")
    fechaCreacion=models.DateField(verbose_name="Fecha", help_text=u"MM/DA/AAAA")
    class Estado(models.TextChoices):
        ACTIVO=1, _('Activo')
        INACTIVO=0, _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
 