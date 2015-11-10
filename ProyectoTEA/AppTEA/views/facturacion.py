# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista del Profesional para mostrar información de facturación.
"""
@login_required(login_url="/loguearse")
def mostrar(request):
    return render(request, 'profesional/facturacion/index.html', {})

