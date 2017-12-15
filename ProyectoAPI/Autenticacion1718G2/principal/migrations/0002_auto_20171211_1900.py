# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-11 18:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genre',
            field=models.CharField(choices=[('MASCULINO', 'masculino'), ('FEMENINO', 'femenino')], default='------', max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
