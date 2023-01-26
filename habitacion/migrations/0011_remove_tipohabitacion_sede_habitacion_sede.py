# Generated by Django 4.1.5 on 2023-01-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0010_remove_habitacion_sede_tipohabitacion_sede'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipohabitacion',
            name='sede',
        ),
        migrations.AddField(
            model_name='habitacion',
            name='sede',
            field=models.CharField(choices=[('estacion', 'La Estación'), ('bosque', 'El Bosque')], max_length=8, null=True, verbose_name='Sede'),
        ),
    ]
