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
from django.views.generic.base import RedirectView


V = 'AppTEA.views.'


urlpatterns = [
    # Redireccion a la pagina de pacientes
    url(r'^$', RedirectView.as_view(url='pacientes/', permanent=True)),

    url(r'^loguearse/$', V + 'usuario.loguearse', name='loguearse'),
    url(r'^desloguearse/$', V + 'usuario.desloguearse', name='desloguearse'),

    url(r'^pacientes/$', V + 'paciente.pacientes', name='pacientes'),
    url(r'^pacientes/registrar/$', V + 'paciente.registrar', name='registrarPaciente'),
    url(r'^pacientes/(?P<id_paciente>\d+)/$', V + 'paciente.ver', name='verPaciente'),
    url(r'^pacientes/(?P<id_paciente>\d+)/editar/$', V + 'paciente.editar', name='editarPaciente'),
    url(r'^pacientes/(?P<id_paciente>\d+)/desactivar/$', V + 'paciente.desactivar', name='desactivarPaciente'),
    
    url(r'^pacientes/(?P<id_paciente>\d+)/historia/$', V + 'paciente.historia.informes', name='historia'),
    url(r'^pacientes/(?P<id_paciente>\d+)/historia/registrar/$', V + 'paciente.historia.registrar', name='registrarInforme'),
    url(r'^pacientes/(?P<id_paciente>\d+)/historia/(?P<id_informe>\d+)/$', V + 'paciente.historia.ver', name='verInforme'),
    url(r'^pacientes/(?P<id_paciente>\d+)/historia/(?P<id_informe>\d+)/editar/$', V + 'paciente.historia.editar', name='editarInforme'),
    url(r'^pacientes/(?P<id_paciente>\d+)/historia/(?P<id_informe>\d+)/desactivar/$', V + 'paciente.historia.desactivar', name='desactivarInforme'),

    url(r'^pacientes/(?P<id_paciente>\d+)/presupuestos/$', V + 'paciente.presupuesto.presupuestos', name='presupuestos'),
    #url(r'^pacientes/(?P<id_paciente>\d+)/presupuestos/registrar/$', V + 'paciente.presupuesto.registrar', name='registrarPresupuesto'),
    #url(r'^pacientes/(?P<id_paciente>\d+)/presupuestos/(?P<id_presupuesto>\d+)/$', V + 'paciente.presupuesto.ver', name='verPresupuesto'),
    #url(r'^pacientes/(?P<id_paciente>\d+)/presupuestos/(?P<id_presupuesto>\d+)/editar/$', V + 'paciente.presupuesto.editar', name='editarPresupuesto'),
    #url(r'^pacientes/(?P<id_paciente>\d+)/presupuestos/(?P<id_presupuesto>\d+)/desactivar/$', V + 'paciente.presupuesto.desactivar', name='desactivarPresupuesto'),


    url(r'^profesionales/$', V + 'profesional.profesionales', name='profesionales'),
    url(r'^profesionales/registrar/$', V + 'profesional.registrar', name='registrarProfesional'),
    url(r'^profesionales/(?P<id_profesional>\d+)/$', V + 'profesional.ver', name='verProfesional'),
    url(r'^profesionales/(?P<id_profesional>\d+)/editar/$', V + 'profesional.editar', name='editarProfesional'),
    url(r'^profesionales/(?P<id_profesional>\d+)/desactivar/$', V + 'profesional.desactivar', name='desactivarProfesional'),

    url(r'^areas/$', V + 'area.areas', name='areas'),
    url(r'^areas/registrar/$', V + 'area.registrar', name='registrarArea'),
    url(r'^areas/(?P<id_area>\d+)/$', V + 'area.ver', name='verArea'),
    url(r'^areas/(?P<id_area>\d+)/editar/$', V + 'area.editar', name='editarArea'),
    url(r'^areas/(?P<id_area>\d+)/desactivar/$', V + 'area.desactivar', name='desactivarArea'),

    url(r'^facturacion/$', V + 'facturacion.mostrar', name='facturacion'),
    url(r'^cobranza/$', V + 'cobranza.mostrar', name='cobranza'),
]
