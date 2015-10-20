# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppTEA.models import Profesional, Area, Paciente
from django.core.context_processors import csrf
import django.contrib.auth.hashers

"""
Página principal del sitio. 

Se puede acceder sólo si el usuario se encuentra logueado, 
de lo contrario se lo redirige a la funcion loguearse.


Una vez logueado el usuario podra ver la lista de pacientes 
y filtrarlos por nombre o apellido.
"""
@login_required(login_url="/loguearse")
def home(request):
    context = { "usuario": request.user,
                "pacientes": Paciente.objects.order_by("nombres"),
                "btn_enlace": "registrar/",
                "btn_icono": "add",}
    
    return render(request, 'home.html', context)

"""
Vista de un paciente particular con sus datos.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def paciente(request, id_paciente):
    context = RequestContext(request)
    # Obtengo el paciente
    paciente = Paciente.objects.get(pk=id_paciente)
    # me fijo si se quiere editar
    if request.method == 'POST':
        modificarPaciente(request, paciente.pk) 
        return redirect("/")   
    else:
    #sino solo lo muestro
        context = {"paciente": paciente}
        return render(request, 'paciente.html', context)
    
    
    

"""
Vista que muestra la historia clínica de un paciente específico.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def historia(request, id_paciente):
    # Obtengo el paciente
    paciente = Paciente.objects.get(pk=id_paciente)
    
    return HttpResponse("historia")

"""
Vista que muestra la lista de presupuestos de distintas fechas 
de un paciente específico.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def presupuestos(request, id_paciente):
    # Obtengo el paciente
    paciente = Paciente.objects.get(pk=id_paciente)
    
    return HttpResponse("presupuestos")

"""
Vista del Administrador para gestionar las áreas existentes.
"""
@login_required(login_url="/loguearse")
def areas(request):
    # Si es Administrador
    if request.user.is_staff:
        context = {"areas": Area.objects.order_by("nombre"),
                   "btn_enlace": "agregar/",
                   "btn_icono": "add" }
        
        return render(request, "administrador/areas.html", context)
    else:
        return HttpResponse("Acceso denegado")

"""
Vista del Administrador para gestionar los profesionales existentes.
"""
@login_required(login_url="/loguearse")
def profesionales(request):
    # Si es Administrador
    if request.user.is_staff:
        context = {"profesionales": Profesional.objects.order_by("first_name"),
                   "btn_enlace": "registrar/",
                   "btn_icono": "add",}
        
        return render(request, "administrador/profesionales.html", context)
    else:
        return HttpResponse("Acceso denegado")


"""
Vista del Profesional para mostrar información de facturación.
"""
@login_required(login_url="/loguearse")
def facturacion(request):
    return HttpResponse("facturacion")


"""
Vista de cobranza.

* En caso de ser Administrador:
    Información de todos los profesionales con sus respectivos aportes.

* En caso de ser Profesional:
    Información de aportes propios.
"""
@login_required(login_url="/loguearse")
def cobranza(request):
    
    return render(request, "cobranza.html")


"""
Vista del Administrador para registrar profesional.
"""
def registrarProfesionales(request):
    context = { "areas" : Area.objects.order_by("nombre").filter(is_active = True),
               "btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
            
#                'asi con todos'
        fieldarea = request.POST['area']
        fieldrnp = request.POST['rnp']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fieldcontra = make_password(request.POST['contra'])
        fieldmail = request.POST['mail']
        fielddni = request.POST['dni']
        fieldnum_matricula = request.POST['num_matricula']
        fieldtel_personal = request.POST['tel_personal']
            
        nuevoProfesional = Profesional(area = fieldarea, rnp = fieldrnp, first_name = fieldnombres, last_name = fieldapellidos, password = fieldcontra, email = fieldmail, dni = fielddni, num_matricula = fieldnum_matricula, tel_personal = fieldtel_personal)
        nuevoProfesional.save()
        return redirect("/home")
    else:
        return render(request, "administrador/registrarProfs.html",context)

"""
Vista del Administrador para registrar paciente.
"""
def registrarPacientes(request):
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
            
#                'asi con todos'
        fielddni = request.POST['dni']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fielddiagnostico = request.POST['diagnostico']
        fieldobra_social = request.POST['obra_social']
        fieldfecha_nacimiento = request.POST['fecha_nacimiento']
        fieldnumero_afiliado = request.POST['numero_afiliado']
        if request.POST['foto']: 
            fieldfoto = request.POST['foto']                
            nuevoPaciente = Paciente(dni = fielddni, nombres = fieldnombres, apellidos = fieldapellidos,diagnostico = fielddiagnostico, obra_social = fieldobra_social, foto = fieldfoto, fecha_nacimiento = fieldfecha_nacimiento, numero_afiliado = fieldnumero_afiliado)
        else:
            nuevoPaciente = Paciente(dni = fielddni, nombres = fieldnombres, apellidos = fieldapellidos,diagnostico = fielddiagnostico, obra_social = fieldobra_social, fecha_nacimiento = fieldfecha_nacimiento, numero_afiliado = fieldnumero_afiliado)
        nuevoPaciente.save()
        return redirect("/")
    else:
        return render(request, "administrador/registrarPacientes.html", context)

"""
Vista del Administrador para modificar paciente.
"""
def modificarPaciente(request, id_paciente):
    pacienteM = Paciente.objects.get(pk = id_paciente)
    
    fielddni = request.POST['dni']
    fieldnombres = request.POST['nombres']
    fieldapellidos = request.POST['apellidos']
    fielddiagnostico = request.POST['diagnostico']
    fieldobra_social = request.POST['obra_social']
    fieldfecha_nacimiento = request.POST['fecha_nacimiento']
    fieldnumero_afiliado = request.POST['numero_afiliado']
    fieldfoto = request.POST['foto']
    
    pacienteM.dni = fielddni
    pacienteM.nombres = fieldnombres
    pacienteM.apellidos = fieldapellidos
    pacienteM.diagnostico = fielddiagnostico
    pacienteM.obra_social = fieldobra_social
    pacienteM.fecha_nacimiento = fieldfecha_nacimiento
    pacienteM.numero_afiliado = fieldnumero_afiliado
    pacienteM.foto = fieldfoto
    pacienteM.save()
    

    
"""
Vista del Administrador para desactivar paciente.
"""    
def desactivarPaciente(request, id_paciente):
    paciente = Paciente.objects.get(pk = id_paciente)
    if paciente.is_active == True:
        paciente.is_active = False
        paciente.save()
        return redirect("/pacientes")
    else:
        return  HttpResponse("el paciente ya esta inactivo")
"""
Vista del Administrador para dar de baja profesional.
"""
def darDeBajaProfesional(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if profesional.is_active == True:
        profesional.is_active = False
        profesional.save()
        return redirect("/profesionales")
    else:
        return HttpResponse("el usuario ya esta inactivo")

"""
Vista del Administrador para editar profesional.
"""
def editarProfesional(reuest, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    
    fieldrnp = request.POST['rnp']
    fieldnombres = request.POST['nombres']
    fieldapellidos = request.POST['apellidos']
    fieldcontra = request.POST['contra']
    fieldmail = request.POST['mail']
    fielddni = request.POST['dni']
    fieldprofesion = request.POST['profesion']
    fieldnum_matricula = request.POST['num_matricula']
    fieldtel_personal = request.POST['tel_personal']
    
    profesional.rnp = fieldrnp
    Profesional.first_name = fieldnombres
    profesional.last_name = fieldapellidos
    profesional.password = fieldcontra
    profesional.email = fieldmail
    profesional.dni = fielddni
    profesional.profesion = fieldprofesion
    profesional.num_matricula = fieldnum_matricula
    profesional.tel_personal = fieldtel_personal
    profesional.save()


"""
Sistema de logueo de usuarios.
"""
def loguearse(request):
    context = RequestContext(request)
        
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Usuario y contrasena
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)

		return redirect('/')


            else:
                # An inactive account was used - no logging in!
                return HttpResponse("ERROR: cuenta inactiva.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:

	# No context variables to pass to the template system, hence the
	# blank dictionary object...
	
	return render_to_response('login.html', context)

"""
Sistema de deslogueo de usuarios.
"""
def desloguearse(request):
    logout(request)
    
    return redirect('/')

def agregarArea(request):
    context = {"btn_enlace": "..",
               "btn_icono": "arrow_back"}
    if request.method == 'POST':
        fieldnombre = request.POST['nombre']
        nuevaArea = Area(nombre = fieldnombre)
        nuevaArea.save()
        return redirect("..")
    else:
        return render(request, "administrador/agregarArea.html", context)
