from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres", null=True) 
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos", null=True)
    class TipoDocumento(models.TextChoices):
        CC='Cédula de Ciudadanía', ('Cédula de Ciudadanía')
        CE='Cédula de Extranjería', ('Cédula de Extranjería')
        PP='Pasaporte', ('Pasaporte')
    tipoDocumento=models.CharField(max_length=25, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.IntegerField(  verbose_name="Número de Documento", null=True)
    email= models.EmailField(max_length=150, verbose_name='correo',null=False)
    telefono=models.IntegerField( verbose_name="Teléfono", null=False,blank=False)
    
    def __str__(self):
        return "Cliente %s" % (self.fechaIngreso)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'