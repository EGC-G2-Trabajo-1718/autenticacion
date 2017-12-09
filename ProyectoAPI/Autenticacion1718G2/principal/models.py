# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


ROLES=(('ASISTENTE','asistente'),('PONENTE',"ponente"))

class User(AbstractUser):
    pass
    genre = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLES, default='ASISTENTE')
    age = models.PositiveIntegerField()
    autonomous_community = models.CharField(max_length=30)
    name = User.first_name
    surname = User.last_name
    
    
