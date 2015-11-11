# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Página principal del sitio. 

Se puede acceder sólo si el usuario se encuentra logueado, 
de lo contrario se lo redirige a la funcion loguearse.


Una vez logueado el usuario podra ver la lista de pacientes 
y filtrarlos por nombre o apellido.
"""
@login_required(login_url="/loguearse")
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
                    "btn_enlace": "registrar/",
                    "btn_icono": "add",
                    "placeholder": "Nombre o apellido",
                    "url_filtro": reverse('apptea:pacientes')}

        return render(request, 'comun/pacientes/index.html', context)


"""
Vista del Administrador para registrar paciente.
"""
def registrar(request):
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
        fielddni = request.POST['dni']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fielddiagnostico = request.POST['diagnostico']
        fieldobra_social = request.POST['obra_social']
        fieldfecha_nacimiento = request.POST['fecha_nacimiento']
        fieldnumero_afiliado = request.POST['numero_afiliado']
        
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
Vista de un paciente particular con sus datos.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def ver(request, id_paciente):
    paciente = Paciente.objects.get(pk=id_paciente)

    context = {"paciente": paciente,
                "btn_enlace": "..",
                "btn_icono": "arrow_back"}

    return render(request, 'comun/pacientes/ver.html', context)


"""
Vista del Administrador para modificar paciente.
"""
def editar(request, id_paciente):
    paciente = Paciente.objects.get(pk = id_paciente)
    if request.POST:
        fielddni = request.POST['dni']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fielddiagnostico = request.POST['diagnostico']
        fieldobra_social = request.POST['obra_social']
        fieldfecha_nacimiento = request.POST['fecha_nacimiento']
        fieldnumero_afiliado = request.POST['numero_afiliado']

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
def desactivar(request, id_paciente):
    paciente = Paciente.objects.get(pk = id_paciente)
    if paciente.is_active == True:
        paciente.is_active = False
        paciente.save()
        return redirect("/")
    else:
        return  HttpResponse("el paciente ya esta inactivo")

