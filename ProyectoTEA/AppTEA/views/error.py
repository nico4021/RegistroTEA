# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista de error para acceso denegado.
"""
@login_required
def denegado(request):
    return render(request, "errores/acceso_denegado.html")
