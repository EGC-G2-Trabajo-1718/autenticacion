# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


ROLES=(('ASISTENTE','asistente'),('PONENTE',"ponente"),('AMBOS','ambos'))
GENEROS=(('MASCULINO','masculino'),('FEMENINO',"femenino"))

class Usuario(models.Model):
    usuario = models.OneToOneField(User, primary_key=True)
    username = models.CharField(max_length=50)
    genre = models.CharField(max_length=20,choices=GENEROS, default='-----')
    role = models.CharField(max_length=10, choices=ROLES, default='ASISTENTE')
    age = models.PositiveIntegerField()
    autonomous_community = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    
    def __unicode__(self):
        return self.name
    

    
    
