# Generated by Django 4.1.5 on 2023-01-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0002_alter_habitacion_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipohabitacion',
            name='descripcion',
            field=models.TextField(max_length=200, verbose_name='Descripcion Habitacion'),
        ),
    ]