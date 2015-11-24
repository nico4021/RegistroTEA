# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista de cobranza.

* En caso de ser Administrador:
    Información de todos los profesionales con sus respectivos aportes.

* En caso de ser Profesional:
    Información de aportes propios.
"""
@login_required
def mostrar(request):
    meses_aporte = []
    mes_year = datetime.now().strftime('%Y-%m')
    objects = Mes_presupuesto.objects.filter()
    for mes_aporte in objects:
        if mes_aporte.mes.strftime('%Y-%m') == mes_year:
            meses_aporte.append(mes_aporte)
            
    context = {
               "meses_aporte":meses_aporte
               }
                      
    return render(request, "comun/cobranza/index.html", context)
