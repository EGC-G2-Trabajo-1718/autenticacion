"""Autenticacion1718G2 URL Configuration

The `urlpatterns` list routes URLs to views2. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views2
    1. Add an import:  from my_app import views2
    2. Add a URL to urlpatterns:  url(r'^$', views2.home, name='home')
Class-based views2
    1. Add an import:  from other_app.views2 import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from principal import views2
from rest_framework.urlpatterns import format_suffix_patterns
from principal.views2 import PostUser
from rest_framework.authtoken import views



post_list = views2.PostUser.as_view({
    'get': 'list',
    'post': 'create'
})



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getUsers/$', views2.getUsers),
    url(r'^getUser/(.+)/$', views2.getUser),
    url(r'^getRoleUser/(.+)/$', views2.getRoleUser),
    url(r'^getUsersByRole/(.+)/$', views2.getUsersByRole),
    url(r'^postUser/$', post_list, name='post_list'), 

    url(r'^crearToken/',views2.crearToken), 
#     url(r'^loguearte/',views2.loguearte), 
    url(r'^api-token-auth/', views.obtain_auth_token),
    #token
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),


]
