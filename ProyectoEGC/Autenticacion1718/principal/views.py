# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404
from principal.models import Usuario
from django.template import RequestContext
from principal.serializers import UserSerializer, RoleSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User 
from rest_framework.authentication import TokenAuthentication
#from django.core.context_processors import request
from lib2to3.fixes.fix_input import context
#from django.contrib.auth.tests.forms import UserCreationFormTest
from django.http.response import HttpResponseRedirect
# Create your views here.


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from re import template
import os
import jinja2
from allauth.account.views import email

def index_view(request):
    if request.method=='POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']
            acceso =authenticate(username=usuario, password=clave)
            if acceso.is_active:
                login(request,acceso)
                return HttpResponseRedirect('/privado')
            else:
                return render_to_response('noactivo.html')
        else:
            return render_to_response('nousuario.html')
    else:
            formulario=AuthenticationForm()
            return render_to_response('index.html',{'formulario':formulario})
        
    return render_to_response('index.html')


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
        
        
        
        
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)





def get(self):
    template=JINJA_ENVIRONMENT.getTemplate('index.html')
    self.response.write(template.render({
        'email':self.EMAIL ,
        'contrasenia' :self.CONTRASENIA,
        }))
    



@csrf_exempt
def getUsers(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def getUser(request, usern):
    if request.method == 'GET':
        # dato = get_object_or_404(Usuario, username=usern)
        usuario = Usuario.objects.get(username=usern)
        serializer = UserSerializer(usuario)
        return JSONResponse(serializer.data)

    
@csrf_exempt
def getRoleUser(request, usern):
    if request.method == 'GET':
        usuario = Usuario.objects.get(username=usern)
        rol = usuario.role
        r = 'True'
        m = 'Successfull'
        serializer = RoleSerializer({'result':r, 'msg':m, 'role':rol})
        return JSONResponse(serializer.data)
    
    
@csrf_exempt
def getUsersByRole(request, rol):
    if request.method == 'GET':
        usuarios = Usuario.objects.filter(role=rol)
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)
    
