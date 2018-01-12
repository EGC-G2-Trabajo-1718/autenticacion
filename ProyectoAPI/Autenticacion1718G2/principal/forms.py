
'''
Created on 12 ene. 2018

@author: Jose Carlos
'''

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'age',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'age': 'age',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }