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
    url(r'^(?P<id_paciente>\d+)/$', 'AppTEA.views.paciente', name='paciente'),
    url(r'^(?P<id_paciente>\d+)/historia/$', 'AppTEA.views.historia', name='historia'),
    url(r'^(?P<id_paciente>\d+)/presupuestos/$', 'AppTEA.views.presupuestos', name='presupuestos'), 
    
    # Urls del administrador
    url(r'^(?P<id_paciente>\d+)/editar$', 'AppTEA.views.modificarPaciente', name='editarPac'),
    url(r'^(?P<id_paciente>\d+)/eliminar$', 'AppTEA.views.desactivarPaciente', name='desactivarPac'),
    url(r'^areas/$', 'AppTEA.views.areas', name='areas'),
    url(r'^areas/agregar/$', 'AppTEA.views.agregarArea', name='agregarArea'),
    url(r'^areas/(?P<id_area>\d+)/$', 'AppTEA.views.editarArea', name='editarArea'),
    url(r'^areas/(?P<id_area>\d+)/desactivar/$', 'AppTEA.views.desactivarArea', name='desactivarArea'),
    url(r'^profesionales/$', 'AppTEA.views.profesionales', name='profesionales'),
    url(r'^profesionales/(?P<id_profesional>\d+)/$', 'AppTEA.views.editarProfesional', name='editarProf'),
#    url(r'^profesionales/(?P<id_profesional>\d+)/eliminar$', 'AppTEA.views.desactivarProfesional', name='desactivarProf'),
    url(r'^profesionales/registrar/$', 'AppTEA.views.registrarProfesionales', name='registrarProf'),
    url(r'^registrar/$', 'AppTEA.views.registrarPacientes', name='registrarPac'),
#    url(r'^desactivarPac/$', 'AppTEA.views.desactivarPac', name='desactivarPac'),
#    url(r'^desactivarProf/$', 'AppTEA.views.desactivarProf', name='desactivarProf'),

    
    # Urls del profesional
    url(r'^(?P<id_paciente>\d+)/historia/nuevoInforme/$', 'AppTEA.views.crearInforme', name='nuevoInforme'),
    url(r'^(?P<id_paciente>\d+)/historia/informe/(?P<id_informe>\d+)$', 'AppTEA.views.verInforme', name='informe'),
    url(r'^(?P<id_paciente>\d+)/historia/editarInforme/(?P<id_informe>\d+)$', 'AppTEA.views.editarInforme', name='editarInforme'),
    url(r'^(?P<id_paciente>\d+)/historia/eliminarInforme/(?P<id_informe>\d+)$', 'AppTEA.views.desactivarInforme', name='desactivarInforme'),
    url(r'^facturacion/$', 'AppTEA.views.facturacion', name='facturacion'),
]
