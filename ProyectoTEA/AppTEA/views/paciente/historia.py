# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista que muestra la historia clínica de un paciente específico.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def informes(request, id_paciente):
    paciente = Paciente.objects.get(pk=id_paciente)
    informes = Informe.objects.filter(is_active = True).filter(paciente = id_paciente).order_by("profesional")
    areas = Area.objects.filter(is_active = True).order_by("nombre")
    
    if request.user.is_staff:
        context = {"areas":areas,
            "informes":informes,
            "paciente":paciente,
            "btn_enlace": "..",
            "btn_icono": "arrow_back"}
    else:
        context = {"areas":areas,
                "informes":informes,
                "paciente":paciente,
                "btn_enlace": "registrar/",
                "btn_icono": "add"}
    return render(request, 'comun/pacientes/historia/index.html', context)


"""
Vista para registrar un nuevo informe.
"""
def registrar(request, id_paciente):
    profesionalObj = Profesional.objects.get(pk=request.user.id)

    if request.POST:
        fieldContenido = request.POST["contenido"]
        fieldPaciente = Paciente.objects.get(pk=id_paciente)
        area = profesionalObj.area
            
        nuevoInforme = Informe(paciente=fieldPaciente, profesional=profesionalObj, area=area, contenido=fieldContenido)
        nuevoInforme.save()
        return redirect("..")
    
    else:
        context = {"btn_enlace": "..",
               "btn_icono": "arrow_back",
               "paciente": Paciente.objects.get(pk=id_paciente),
               "profesional": profesionalObj}
        return render(request, "comun/pacientes/historia/registrar.html", context)


"""
Vista de un informe específico.
"""
@login_required(login_url="/loguearse")
def ver(request, id_paciente, id_informe):
    informe = Informe.objects.get(pk = id_informe)
    context = {
        "informe": informe,
        "btn_enlace": "..",
        "btn_icono": "arrow_back"        
    }
    return render(request, "comun/pacientes/historia/ver.html", context)


"""
Editar un informe
"""
def editar(request, id_paciente, id_informe):
    informe = Informe.objects.get(pk=id_informe)
    if request.POST:
        fieldContenido = request.POST['contenido']
        informe.contenido = fieldContenido
        informe.save()
        return redirect("..")
    else:
        context = {
            "informe": informe,
            "btn_enlace": "../..",
            "btn_icono": "arrow_back",
            "profesional": Profesional.objects.get(pk=request.user.id)
        }
        return render(request, "comun/pacientes/historia/editar.html", context)


"""
Vista para desactivar informe.
"""
def desactivar(request, id_informe):
    informe = Informe.objects.get(pk=id_informe)
    informe.is_active = False
    informe.save()
    return redirect(".")
