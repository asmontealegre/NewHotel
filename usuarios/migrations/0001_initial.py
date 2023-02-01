# Generated by Django 4.1.5 on 2023-01-31 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioTipo', models.CharField(choices=[('Administrador', 'Administrador'), ('Recepción', 'Recepción')], default='Recepción', max_length=14, verbose_name='Usuario Tipo')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=150, verbose_name='correo')),
                ('tipoDocumento', models.CharField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'), ('Cédula de Extranjería', 'Cédula de Extranjería'), ('Pasaporte', 'Pasaporte'), ('Tarjeta de Identidad', 'Tarjeta de Identidad'), ('Otro Tipo de Documento', 'Otro Tipo de Documento')], default='Cédula de Ciudadanía', max_length=25, verbose_name='Tipo de Documento')),
                ('numeroDocumento', models.CharField(max_length=45, unique=True, verbose_name='Número de Documento')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='Teléfono')),
                ('rol', models.CharField(choices=[('Recepción', 'Recepción'), ('Administración', 'Administración')], default='Recepción', max_length=25, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
