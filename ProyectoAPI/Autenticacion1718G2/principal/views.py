# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404
from principal.models import Usuario
from django.template import RequestContext
from principal.serializers import UserSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def getUsers(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def getUser(request, usern):
    if request.method == 'GET':
        dato = get_object_or_404(Usuario, username=usern)
        usuario = Usuario.objects.filter(username=dato)
        serializer = UserSerializer(usuario)
        return JSONResponse(serializer.data)