# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista de cobranza.

* En caso de ser Administrador:
    Información de todos los profesionales con sus respectivos aportes.

* En caso de ser Profesional:
    Información de aportes propios.
"""
@login_required(login_url="/loguearse")
def mostrar(request):
    
    return render(request, "comun/cobranza/index.html")
