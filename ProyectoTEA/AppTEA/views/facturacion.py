# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista del Profesional para mostrar información de facturación.
"""
@login_required(login_url="/loguearse")
def mostrar(request):
	context = {
		"pacientes": Paciente.objects.filter(),
	}
	return render(request, 'profesional/facturacion/index.html', context)

