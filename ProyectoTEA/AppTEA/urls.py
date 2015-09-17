"""AppTEA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Urls comunes
    url(r'^$', 'AppTEA.views.home', name='home'),
    url(r'^loguearse/$', 'AppTEA.views.loguearse', name='loguearse'),
    url(r'^desloguearse/$', 'AppTEA.views.desloguearse', name='desloguearse'),
    url(r'^cobranza/$', 'AppTEA.views.cobranza', name='cobranza'),
    
    # Urls del administrador
    url(r'^paciente/(?P<id_paciente>\d+)/$', 'AppTEA.views.paciente', name='paciente'),
    url(r'^paciente/(?P<id_paciente>\d+)/historia/$', 'AppTEA.views.historia', name='historia'),
    url(r'^paciente/(?P<id_paciente>\d+)/presupuestos/$', 'AppTEA.views.presupuestos', name='presupuestos'), 
    url(r'^areas/$', 'AppTEA.views.areas', name='areas'),
    url(r'^profesionales/$', 'AppTEA.views.profesionales', name='profesionales'),
    
    # Urls del profesional
    url(r'^pacientes/$', 'AppTEA.views.pacientes', name='pacientes'),
    url(r'^facturacion/$', 'AppTEA.views.facturacion', name='facturacion'),
]
