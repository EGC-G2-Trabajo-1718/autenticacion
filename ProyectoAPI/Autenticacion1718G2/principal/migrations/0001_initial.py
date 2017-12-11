# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 17:46
from __future__ import unicode_literals

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
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('ASISTENTE', 'asistente'), ('PONENTE', 'ponente'), ('AMBOS', 'ambos')], default='ASISTENTE', max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('autonomous_community', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
