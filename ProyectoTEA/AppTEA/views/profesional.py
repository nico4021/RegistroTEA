# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista del Administrador para gestionar los profesionales existentes.
"""
@login_required(login_url="/loguearse")
def profesionales(request):
    # Si es Administrador
    if request.user.is_staff:

        if (request.method == "POST"):
            filtro = request.POST['filtro']
            profesionales = Profesional.objects.filter(Q(first_name__icontains=filtro) | Q(last_name__icontains=filtro),
                                                is_active=True).order_by("first_name")
            json = []

            for prof in range(len(profesionales)):
                json.append({'id': profesionales[prof].id,
                         'nombres': profesionales[prof].first_name,
                         'apellidos': profesionales[prof].last_name,
                         'dni': profesionales[prof].dni})

            return JsonResponse({"cards": json})
        
        else:
            context = {"profesionales": Profesional.objects.filter(is_active=True).order_by("first_name"),
                       "btn_enlace": "registrar/",
                       "btn_icono": "add",
                       "placeholder": "Nombre o apellido",
                       "funcion_filtro": "funcionPacProf"}
            
            return render(request, "administrador/profesionales/index.html", context)
    else:
        return HttpResponse("Acceso denegado")


"""
Vista del Administrador para registrar profesional.
"""
def registrar(request):
    context = { "areas" : Area.objects.order_by("nombre").filter(is_active = True),
               "btn_enlace": "..",
               "btn_icono": "arrow_back"}

    if request.method == 'POST':
        fieldarea = Area.objects.get(pk=int(request.POST['area']))
        fieldrnp = request.POST['rnp']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fieldcontra = make_password(request.POST['contra'])
        fieldmail = request.POST['mail']
        fielddni = request.POST['dni']
        fieldnum_matricula = request.POST['num_matricula']
        fieldtel_personal = request.POST['tel_personal']
        fieldusername = request.POST['usuario']
            
        nuevoProfesional = Profesional(username=fieldusername ,area=fieldarea, rnp=fieldrnp, first_name=fieldnombres, last_name=fieldapellidos, password=fieldcontra, email=fieldmail, dni=fielddni, num_matricula=fieldnum_matricula, tel_personal=fieldtel_personal)
        nuevoProfesional.save()
        return redirect("..")
    else:
        return render(request, "administrador/profesionales/registrar.html", context)


"""
Vista del Administrador para ver un profesional.
"""
def ver(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back",
               "profesional":profesional}

    return render(request, "administrador/profesionales/ver.html", context)
	

"""
Vista del Administrador para editar profesional.
"""
def editar(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if request.POST:
        fieldarea = request.POST['area']
        fieldrnp = request.POST['rnp']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fieldmail = request.POST['mail']
        fielddni = request.POST['dni']
        fieldnum_matricula = request.POST['num_matricula']
        fieldtel_personal = request.POST['tel_personal']
        
        profesional.area = Area.objects.get(pk=int(fieldarea))
        profesional.rnp = fieldrnp
        Profesional.first_name = fieldnombres
        profesional.last_name = fieldapellidos
        profesional.email = fieldmail
        profesional.dni = fielddni
        profesional.num_matricula = fieldnum_matricula
        profesional.tel_personal = fieldtel_personal
        
        try:
            fieldpass = request.POST['contra']
            profesional.password = fieldpass
        except MultiValueDictKeyError:
            print request.POST

        profesional.save()
        return redirect("/profesionales")
    else:
        context = {"btn_enlace": "../..",
               "btn_icono": "arrow_back",
               "profesional":profesional,
               "areas" : Area.objects.order_by("nombre").filter(is_active = True)}
               
        return render(request, "administrador/profesionales/editar.html", context)


    
"""
Vista del Administrador para dar de baja profesional.
"""
def desactivar(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if profesional.is_active == True:
        profesional.is_active = False
        profesional.save()
        return redirect("/profesionales")
    else:
        return HttpResponse("el usuario ya esta inactivo")

