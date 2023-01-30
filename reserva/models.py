from django.db import models

from habitacion.models import Habitacion

# Create your models here.
class Check(models.Model):
    id = models.AutoField(primary_key = True)
    check_in = models.DateField(verbose_name="Check_in", help_text=u"MM/DA/AAAA",null=True, blank=True)
    check_out = models.DateField(verbose_name="Check_out", help_text=u"MM/DA/AAAA",null=True, blank=True)
    cantNoches= models.IntegerField(verbose_name='Cantidad Noches')
    Habitacion_id = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitación",null=True)

    def __str__(self):
        return "Check %s" % (self.check_in)

    class Meta:
        verbose_name = 'Check'
        verbose_name_plural = 'Check'
        

class Reserva(models.Model):
    id = models.AutoField(primary_key = True)
    fechaIngreso=models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso", help_text=u"MM/DA/AAAA",null=True, blank=True)
    cantidadHabitaciones = models.PositiveIntegerField('Cantidad o Stock', default = 1)
    numeroHuespedes =models.IntegerField(verbose_name='Numero de Huéspedes')
    valorReserva = models.BigIntegerField(verbose_name='Valor Reserva')
    Check_id = models.ForeignKey(Check, on_delete=models.CASCADE, verbose_name="Cliente",null=True)

    def __str__(self):
        return "Reserva %s" % (self.fechaIngreso)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        

class DetalleReserva(models.Model):
    id = models.AutoField(primary_key = True)
    Habitacion_id = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitación",null=True)
    Reserva_id = models.ForeignKey(Reserva, on_delete=models.CASCADE, verbose_name="Reserva",null=True)
    
    def __str__(self):
        return "DetalleReserva %s" % (self.Habitacion_id)

    class Meta:
        verbose_name = 'DetalleReserva'
        verbose_name_plural = 'DetallesReservas'
