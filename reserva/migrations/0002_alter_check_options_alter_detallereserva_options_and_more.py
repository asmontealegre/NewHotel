# Generated by Django 4.1.5 on 2023-01-29 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'verbose_name': 'Check', 'verbose_name_plural': 'Check'},
        ),
        migrations.AlterModelOptions(
            name='detallereserva',
            options={'verbose_name': 'DetalleReserva', 'verbose_name_plural': 'DetallesReservas'},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]
