# Generated by Django 4.1.5 on 2023-01-26 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0013_alter_habitacion_tipohabitacion_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habitacion',
            old_name='TipoHabitacion_id',
            new_name='TipoHabitacion',
        ),
    ]
