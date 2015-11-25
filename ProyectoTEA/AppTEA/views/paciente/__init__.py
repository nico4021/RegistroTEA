# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Página principal del sitio. 

Se puede acceder sólo si el usuario se encuentra logueado, 
de lo contrario se lo redirige a la funcion loguearse.


Una vez logueado el usuario podra ver la lista de pacientes 
y filtrarlos por nombre o apellido.
"""
@login_required
def pacientes(request):
    
    if request.method == "POST" and request.is_ajax():
        filtro = request.POST['filtro']
        pacientes = Paciente.objects.filter(Q(nombres__icontains=filtro) | Q(apellidos__icontains=filtro),
                                            is_active=True).order_by("nombres")
        ids = []

        for p in pacientes:
            ids.append(p.id)

        return JsonResponse({"ids": ids})

    else:
        pacientes = Paciente.objects.filter(is_active=True).order_by("nombres")

        context = { "usuario": request.user,
                    "pacientes": pacientes,
                    "placeholder": "Nombre o apellido",
                    "url_filtro": reverse('apptea:pacientes')}
        if request.user.is_staff:
            context["btn_enlace"] = "registrar/"
            context["btn_icono"] = "add"
            
        return render(request, 'comun/pacientes/index.html', context)

"""
Vista de un paciente particular con sus datos.

Recibe como parámetro el id del paciente.
"""
@login_required
def ver(request, id_paciente):
    paciente = Paciente.objects.get(pk=id_paciente)

    context = {"paciente": paciente,
                "btn_enlace": "..",
                "btn_icono": "arrow_back"}

    return render(request, 'comun/pacientes/ver.html', context)


"""
Vista del Administrador para registrar paciente.
"""
@permission_required('AppTEA.add_paciente', raise_exception=True)
def registrar(request):
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
        try: 
            fielddni = request.POST['dni']
            if fielddni == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldnombres = request.POST['nombres']
            if fieldnombres == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldapellidos = request.POST['apellidos']
            if fieldapellidos == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fielddiagnostico = request.POST['diagnostico']
            if fielddiagnostico == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldobra_social = request.POST['obra_social']
            if fieldobra_social == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldfecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento'], "%d/%m/%Y").date()
            fieldnumero_afiliado = request.POST['numero_afiliado']
            if fieldnumero_afiliado == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
        except ValueError as e:
            print e
            context['err'] = "Formato de Fecha Invalido"
            return render(request, "comun/pacientes/registrar.html", context)
            
        paciente = Paciente()

        try: 
            request.FILES['foto']
            fieldfoto = request.FILES['foto']                
            paciente.foto = fieldfoto
        except: pass

        paciente.dni = fielddni
        paciente.nombres = fieldnombres
        paciente.apellidos = fieldapellidos
        paciente.diagnostico = fielddiagnostico
        paciente.obra_social = fieldobra_social
        paciente.fecha_nacimiento = fieldfecha_nacimiento
        paciente.numero_afiliado = fieldnumero_afiliado
        paciente.save()
        return redirect("/")
    else:
        return render(request, "comun/pacientes/registrar.html", context)


"""
Vista del Administrador para modificar paciente.
"""
@permission_required('AppTEA.change_paciente', raise_exception=True)
def editar(request, id_paciente):
    paciente = Paciente.objects.get(pk = id_paciente)
    if request.POST:
        try: 
            fielddni = request.POST['dni']
            if fielddni == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldnombres = request.POST['nombres']
            if fieldnombres == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldapellidos = request.POST['apellidos']
            if fieldapellidos == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fielddiagnostico = request.POST['diagnostico']
            if fielddiagnostico == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldobra_social = request.POST['obra_social']
            if fieldobra_social == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
            fieldfecha_nacimiento = datetime.strptime(request.POST['fecha_nacimiento'], "%d/%m/%Y").date()
            fieldnumero_afiliado = request.POST['numero_afiliado']
            if fieldnumero_afiliado == "":
                context['err'] = "Faltan Campos"
                return render(request, "comun/pacientes/registrar.html", context)
        except ValueError as e:
            print e
            context['err'] = "Formato de Fecha Invalido"
            return render(request, "comun/pacientes/registrar.html", context)
        
        
        try: 
            request.FILES['foto']
            fieldfoto = request.FILES['foto']                
            paciente.foto = fieldfoto
        except: pass
        
        paciente.dni = fielddni
        paciente.nombres = fieldnombres
        paciente.apellidos = fieldapellidos
        paciente.diagnostico = fielddiagnostico
        paciente.obra_social = fieldobra_social
        paciente.fecha_nacimiento = fieldfecha_nacimiento
        paciente.numero_afiliado = fieldnumero_afiliado
        paciente.save()
        return redirect('/')
    else:
        context = {"pac": paciente,
                   "btn_enlace": "../..",
                   "btn_icono": "arrow_back"}

        return render(request, 'comun/pacientes/editar.html', context)


"""
Vista del Administrador para desactivar paciente.
"""
@permission_required('AppTEA.delete_paciente', raise_exception=True)
def desactivar(request, id_paciente):
    paciente = Paciente.objects.get(pk = id_paciente)
    if paciente.is_active == True:
        paciente.is_active = False
        paciente.save()
        return redirect("/")
    else:
        return  HttpResponse("el paciente ya esta inactivo")

