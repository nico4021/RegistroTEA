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
    if request.user.is_staff == True:
        objects = Mes_presupuesto.objects.filter()
    else:
        objects = Mes_presupuesto.objects.filter(profesional = request.user.pk)
    for mes_aporte in objects:
        if mes_aporte.mes.strftime('%Y-%m') == mes_year:
            meses_aporte.append(mes_aporte)
            
    context = {
               "meses_aporte":meses_aporte
               }
                      
    return render(request, "comun/cobranza/index.html", context)

def mostrar_todas(request):
    meses_aporte = []
    mes_year = datetime.now().strftime('%Y-%m')
    if request.user.is_staff == True:
        objects = Mes_presupuesto.objects.filter()
    else:
        objects = Mes_presupuesto.objects.filter(profesional = request.user.pk)
        
    context = {
               "btn_enlace": "../cobranza",
               "btn_icono": "arrow_back",
               "titulo": "Cobranza General",
               "meses_aporte":objects
               }
                      
    return render(request, "comun/cobranza/index.html", context)