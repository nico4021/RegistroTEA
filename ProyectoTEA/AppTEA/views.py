# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from AppTEA.models import Profesional, Area, Paciente


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
                "pacientes": Paciente.objects.order_by("nombres"),}
    
    
    return render(request, 'home.html', context)

"""
Vista de un paciente particular con sus datos.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def paciente(request, id_paciente):
    # Obtengo el paciente
    paciente = Paciente.objects.get(pk=id_paciente)
    
    return HttpResponse("paciente")

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
        context = {"areas": Area.objects.order_by("nombre")}
        
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
        context = {"profesionales": Profesional.objects.order_by("nombres")}
        
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
    return HttpResponse("cobranza")


"""
Vista del Administrador para registrar profesional.
"""
def registrarProfesionales(request):
    context = RequestContext(request)
    if request.method == 'POST':
            
#                'asi con todos'
        fieldrnp = request.POST['rnp']
        fieldnombres = request.POST['nombres']
        fieldapellidos = request.POST['apellidos']
        fieldcontra = request.POST['contra']
        fieldmail = request.POST['mail']
        fielddni = request.POST['dni']
        fieldprofesion = request.POST['profesion']
        fieldnum_matricula = request.POST['num_matricula']
        fieldtel_personal = request.POST['tel_personal']
            
        nuevoProfesional = Profesional(rnp = fieldrnp, first_name = fieldnombres, last_name = fieldapellidos, password = fieldcontra, email = fieldmail, dni = fielddni, profesion = fieldprofesion, num_matricula = fieldnum_matricula, tel_personal = fieldtel_personal)
        nuevoProfesional.save()
        return redirect("/home")
    else:
        return render_to_response("registrarProfs.html",context)

"""
Vista del Administrador para dar de baja profesional.
"""
def darDeBajaProfesional(request, id_profesional):
    profesional = Profesional.objects.get(pk = id_profesional)
    if profesional.is_active == True:
        profesional.is_active = False
        profesional.save()
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

