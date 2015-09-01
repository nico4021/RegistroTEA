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
    url(r'^$', 'AppTEA.views.home', name='home'),
    url(r'^loguearse/$', 'AppTEA.views.loguearse', name='loguearse'),
    url(r'^desloguearse/$', 'AppTEA.views.desloguearse', name='desloguearse'),
    url(r'^curso/(?P<id_curso>\d+)/$', 'AppTEA.views.curso', name='curso'),
    url(r'^curso/(?P<id_curso>\d+)/info/$', 'AppTEA.views.info', name='info'),
    url(r'^alumno/(?P<id_alumno>\d+)/$', 'AppTEA.views.alumno', name='alumno'),
]
