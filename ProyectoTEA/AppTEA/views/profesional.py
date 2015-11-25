# -*- coding: utf-8 -*-

from AppTEA.views import *
from django.core.management import call_command


"""
Vista del Administrador para gestionar los profesionales existentes.
"""
@permission_required('AppTEA.profesionales', raise_exception=True)
def profesionales(request):
    # Si es Administrador
    if request.user.is_staff:

        if request.method == "POST" and request.is_ajax():
            filtro = request.POST['filtro']
            profesionales = Profesional.objects.filter(Q(first_name__icontains=filtro) | Q(last_name__icontains=filtro),
                                                is_active=True).order_by("first_name")
            ids = []

            for p in profesionales:
                ids.append(p.id)

            return JsonResponse({"ids": ids})

        else:
            context = {"profesionales": Profesional.objects.filter(is_active=True).order_by("first_name"),
                       "btn_enlace": "registrar/",
                       "btn_icono": "add",
                       "placeholder": "Nombre o apellido",
                       "url_filtro": reverse('apptea:profesionales')}
            
            return render(request, "administrador/profesionales/index.html", context)
    else:
        return HttpResponse("Acceso denegado")


"""
Vista del Administrador para registrar profesional.
"""
@permission_required('AppTEA.profesionales', raise_exception=True)
def registrar(request):
    context = { "areas" : Area.objects.order_by("nombre").filter(is_active = True),
               "btn_enlace": "..",
               "btn_icono": "arrow_back"}

    if request.method == 'POST':
        fieldarea = Area.objects.get(pk=int(request.POST['area']))
        fieldrnp = request.POST['rnp']
        if fieldrnp == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldnombres = request.POST['nombres']
        if fieldnombres == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldapellidos = request.POST['apellidos']
        if fielapellidos == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        if request.POST['contra'] == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldcontra = make_password(request.POST['contra'])
        fieldmail = request.POST['mail']
        if fieldmail == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fielddni = request.POST['dni']
        if fielddni == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldnum_matricula = request.POST['num_matricula']
        if fieldnum_matricula == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldtel_personal = request.POST['tel_personal']
        if fieldtel_personal == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldusername = request.POST['usuario']
        if fieldusername == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        
            
        nuevoProfesional = Profesional(username=fieldusername ,area=fieldarea, rnp=fieldrnp, first_name=fieldnombres, last_name=fieldapellidos, password=fieldcontra, email=fieldmail, dni=fielddni, num_matricula=fieldnum_matricula, tel_personal=fieldtel_personal)
        nuevoProfesional.save()

        call_command('add_groups')

        g = Group.objects.get(name='profesional') 
        g.user_set.add(nuevoProfesional)

        return redirect("..")
    else:
        return render(request, "administrador/profesionales/registrar.html", context)


"""
Vista del Administrador para ver un profesional.
"""
@permission_required('AppTEA.profesionales', raise_exception=True)
def ver(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back",
               "profesional":profesional}

    return render(request, "administrador/profesionales/ver.html", context)
	

"""
Vista del Administrador para editar profesional.
"""
@permission_required('AppTEA.profesionales', raise_exception=True)
def editar(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if request.POST:
        fieldarea = request.POST['area']
        fieldrnp = request.POST['rnp']
        if fieldrnp == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldnombres = request.POST['nombres']
        if fieldnombres == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldapellidos = request.POST['apellidos']
        if fielapellidos == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldmail = request.POST['mail']
        if fieldmail == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fielddni = request.POST['dni']
        if fielddni == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldnum_matricula = request.POST['num_matricula']
        if fieldnum_matricula == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        fieldtel_personal = request.POST['tel_personal']
        if fieldtel_personal == "":
            context['err'] = "faltan campos"
            return render(request, "administrador/profesionales/registrar.html", context)
        
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
@permission_required('AppTEA.profesionales', raise_exception=True)
def desactivar(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if profesional.is_active == True:
        profesional.is_active = False
        profesional.save()
        return redirect("/profesionales")
    else:
        return HttpResponse("el usuario ya esta inactivo")

