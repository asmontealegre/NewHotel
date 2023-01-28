from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
# PQRS.
class PQRS(models.Model):
    id = models.AutoField(primary_key = True)
    fechaIngreso=models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso", help_text=u"MM/DA/AAAA",null=True, blank=True)
    nombres=models.CharField(max_length=45, verbose_name="Nombres",blank=True) 
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos",blank=True)
    telefono=models.CharField(max_length=15, verbose_name="Teléfono",blank=True)
    email=models.CharField(max_length=50, verbose_name="Correo Electronico", blank=True)
    class Asunto(models.TextChoices):
        QUEJA = 'Queja', ('Queja')
        RECLAMO = 'Reclamo', ('Reclamo')
        PETICION = 'Petición', ('Petición')
        SOLICITUD = 'Solicitud', ('Solicitud')
        DENUNCIA= 'Denuncia', ('Denuncia')
        REEMBOLSO = 'Reembolso', ('Reembolso')   
        ESTAFA = 'Estafa',('Estafa')
        ROBO = 'Robo',('Robo')
    asunto=models.CharField(max_length=45, verbose_name="Asunto")
    comentarioCliente=models.CharField(max_length=250, verbose_name="Comentario")
    adjunto=models.CharField(max_length=250, verbose_name="Adjunto")
    class Estado(models.TextChoices):
        ACTIVO=1, _('Activo')
        INACTIVO=0, _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

