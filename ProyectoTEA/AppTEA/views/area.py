# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista del Administrador para gestionar las áreas existentes.
"""
@permission_required('AppTEA.areas', raise_exception=True)
def areas(request):
    # Si es Administrador
    if request.user.is_staff:

        if request.method == "POST" and request.is_ajax():
            filtro = request.POST['filtro']
            areas = Area.objects.filter(Q(nombre__icontains=filtro),
                                                is_active=True).order_by("nombre")
            ids = []

            for a in areas:
                ids.append(a.id)

            return JsonResponse({"ids": ids})

        else:
            context = {"areas": Area.objects.filter(is_active=True).order_by("nombre"),
                       "btn_enlace": "registrar/",
                       "btn_icono": "add",
                       "placeholder": "Nombre del area",
                       "url_filtro": reverse('apptea:areas')}
            
            return render(request, "administrador/areas/index.html", context)
    else:
        return HttpResponse("Acceso denegado")


"""
Vista del Administrador para registrar una nueva area
"""
@permission_required('AppTEA.areas', raise_exception=True)
def registrar(request):
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
        fieldnombre = request.POST['nombre']
        if fieldnombre == "":
            context['err'] = "el nombre esta vacio"
            return render(request, "administrador/areas/editar.html", context)
        nuevaArea = Area(nombre = fieldnombre)
        nuevaArea.save()
        return redirect("..")
    else:
        return render(request, "administrador/areas/registrar.html", context)


"""
Vista del Administrador para ver un area específica
"""
@permission_required('AppTEA.areas', raise_exception=True)
def ver(request, id_area):
    area = Area.objects.get(pk=id_area)
    context = {"area": Area.objects.get(pk=id_area),
               "btn_enlace": "..",
               "btn_icono": "arrow_back"}

    return render(request, "administrador/areas/ver.html", context)


"""
Vista del Administrador para editar un area
"""
@permission_required('AppTEA.areas', raise_exception=True)
def editar(request, id_area):
    area = Area.objects.get(pk=id_area)
    context = {"area": Area.objects.get(pk=id_area),
               "btn_enlace": "../..",
               "btn_icono": "arrow_back"}
               
    if request.method == 'POST':
        if request.POST['nombre'] == "":
            context['err'] = "el nombre esta vacio"
            return render(request, "administrador/areas/editar.html", context)
        area.nombre = request.POST['nombre']
        area.save()
        return redirect("../..")
    else:
        return render(request, "administrador/areas/editar.html", context)

"""
Vista del Administrador para desactivar area.
"""
@permission_required('AppTEA.areas', raise_exception=True)
def desactivar(request, id_area):
    area = Area.objects.get(pk=id_area)
    area.is_active = False
    area.save()
    return redirect("apptea:areas")
