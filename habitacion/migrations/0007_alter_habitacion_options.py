# Generated by Django 4.1.5 on 2023-01-26 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0006_alter_habitacion_estado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habitacion',
            options={'ordering': ['numeroHabitacion'], 'verbose_name': 'Habitacion', 'verbose_name_plural': 'Habitaciones'},
        ),
    ]
