"""Autenticacion1718G2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url
from principal import views
from principal.views import RegistroUsuario
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getUsers/$', views.getUsers),
    url(r'^getUser/(.+)/$', views.getUser),
    url(r'^getRoleUser/(.+)/$', views.getRoleUser),
    url(r'^getUsersByRole/(.+)/$', views.getUsersByRole),
    
    # token
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    
    #Plantillas
    #url(r'^', include('Autenticacion1718G2.principal.urls')),
    #url(r'^$', views.index_view),
    url(r'^$', login, {'template_name':'index.html'}, name='login'),
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    
    url(r'^password_reset_done', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),


    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
     url(r'^', views.nuevo_usuario),
]

    
  
