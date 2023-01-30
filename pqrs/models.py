from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
# PQRS.
class PQRS(models.Model):
    id = models.AutoField(primary_key = True)
    fechaIngreso=models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso", help_text=u"MM/DA/AAAA",null=True, blank=True)
    class TipoDocumento(models.TextChoices):
        CC='Cédula de Ciudadanía', ('Cédula de Ciudadanía')
        CE='Cédula de Extranjería', ('Cédula de Extranjería')
        PP='Pasaporte', ('Pasaporte')
    tipoDocumento=models.CharField(max_length=25, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.IntegerField(  verbose_name="Número de Documento", null=True)
    nombres=models.CharField(max_length=45, verbose_name="Nombres",null=True) 
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos",null=True)
    telefono=models.CharField(max_length=15, verbose_name="Teléfono",null=True)
    email=models.CharField(max_length=50, verbose_name="Correo Electronico", null=True)
    class Asunto(models.TextChoices):
        P= 'Petición', ('Petición')
        Q= 'Queja', ('Queja')
        R= 'Reclamo', ('Reclamo')
        S= 'Solicitud', ('Solicitud')
        D= 'Denuncia', ('Denuncia')
        M= 'Reembolso', ('Reembolso')   
        E= 'Estafa',('Estafa')
        B= 'Robo',('Robo')
    asunto=models.CharField(max_length=45,choices=Asunto.choices,default=Asunto.P, verbose_name="Asunto")
    comentarioCliente=models.CharField(max_length=250, verbose_name="Comentario")
    adjunto=models.FileField('Adjuntar Archivo')
    estado=models.BooleanField('Estado', default=True)
    def __str__(self):
        return "PQRS %s" % (self.nombres)

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'