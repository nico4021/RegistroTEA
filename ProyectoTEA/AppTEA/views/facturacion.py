# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista del Profesional para mostrar información de facturación.
"""
@permission_required('AppTEA.facturacion', raise_exception=True)
def mostrar(request):
	if request.user.is_staff:
		pacientes = Paciente.objects.all()

	else:
		profesional = Profesional.objects.get(pk=request.user.id)

		pacientes = []

		for pres in profesional.presupuesto_set.all():
			if not pres.paciente in pacientes:
				pacientes.append(pres.paciente)

	context = {
		"pacientes": pacientes,
	}
	return render(request, 'profesional/facturacion/index.html', context)
