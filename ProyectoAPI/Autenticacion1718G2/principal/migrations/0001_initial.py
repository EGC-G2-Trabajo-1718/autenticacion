# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-16 08:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('genre', models.CharField(choices=[('MASCULINO', 'masculino'), ('FEMENINO', 'femenino')], default='-----', max_length=20)),
                ('role', models.CharField(choices=[('ASISTENTE', 'asistente'), ('PONENTE', 'ponente'), ('AMBOS', 'ambos')], default='ASISTENTE', max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('autonomous_community', models.CharField(choices=[('ANDALUCIA', 'Andalucia'), ('ARAGON', 'Aragon'), ('ASTURIAS', 'Asturias'), ('CANTABRIA', 'Cantabria'), ('CASTILLA LA MANCHA', 'Castilla la mancha'), ('CASTILLA LEON', 'Castilla leon'), ('EXTREMADURA', 'Extremadura'), ('GALICIA', 'Galicia'), ('LA RIOJA', 'La rioja'), ('MADRID', 'Madrid'), ('MURCIA', 'Murcia'), ('NAVARRA', 'Navarra'), ('PAIS VASCO', 'Pais vasco'), ('VALENCIA', 'Valencia'), ('BALEARES', 'Baleares'), ('CANARIAS', 'Canarias'), ('CEUTA', 'Ceuta'), ('MELILLA', 'Melilla')], default='-----', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
            ],
        ),
    ]
