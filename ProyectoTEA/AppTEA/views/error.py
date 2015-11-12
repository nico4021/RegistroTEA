# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista de error para acceso denegado.
"""
@login_required
def error403(request):
    return render(request, "errores/403.html")

"""
Vista de error para acceso denegado.
"""
@login_required
def error404(request):
    return render(request, "errores/404.html")

"""
Vista de error para acceso denegado.
"""
@login_required
def denegado(request):
    return render(request, "errores/acceso_denegado.html")
