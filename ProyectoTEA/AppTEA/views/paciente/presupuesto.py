# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista que muestra la lista de presupuestos de distintas fechas 
de un paciente específico.

Recibe como parámetro el id del paciente.
"""
@login_required
def presupuestos(request, id_paciente):
    # Obtengo el paciente
    print "la mama de lucho se la come"
    paciente = Paciente.objects.get(pk=id_paciente)
    presupuestos = Presupuesto.objects.filter(paciente = paciente.pk).filter(is_active = True).order_by("fecha_creacion")
    context = {"presupuestos": presupuestos,
                   "btn_enlace": "registrar/",
                   "btn_icono": "add" }
    template = render(request, "comun/pacientes/presupuestos/index.html", context)        
    return template

@login_required
def registrar(request, id_paciente):
    print "la mama de lucho se la come"
    if request.method == 'POST':
        
        
        idProf = int(request.user.pk)
        paciente = Paciente.objects.get(pk = id_paciente)
        profesional = Profesional.objects.get(user_ptr_id = idProf)
        
        # Atributos
        
    
        tratamiento_prestacion = request.POST['tratamiento_prestacion']
        domicilio_prestacion = request.POST['domicilio_prestacion']
        costo_hora = int(request.POST['costo_hora'])
        costo_mensual = 0
        costo_semanal = 0
        fecha_creacion = datetime.now().date() 
        periodo = request.POST['periodo'] 
        texto = request.POST['texto'] 
        
        presupuesto = Presupuesto()
        dias = request.POST.getlist('dia')
        
        for i in range(len(dias)):
            dia = dias[i]
            hora_entrada = request.POST['horario_entrada_'+dia]
            hora_salida = request.POST['horario_salida_'+dia]
            cantidad_horas = int(request.POST['horas_'+dia])
            costo_semanal += cantidad_horas
            horario = Horario(presupuesto = presupuesto, dia = dia, hora_entrada = hora_entrada, hora_salida = hora_salida, cantidad_horas = cantidad_horas)
            horario.save()
        
        costo_mensual = costo_semanal*4
        presupuesto.tratamiento_prestacion = tratamiento_prestacion
        presupuesto.domicilio_prestacion = domicilio_prestacion
        presupuesto.costo_hora = costo_hora
        presupuesto.costo_mensual = costo_mensual
        presupuesto.costo_semanal = costo_semanal
        presupuesto.fecha_creacion = fecha_creacion
        presupuesto.periodo = periodo
        presupuesto.texto = texto
        presupuesto.paciente = paciente
        presupuesto.profesional = profesional
        presupuesto.save()
             
        return redirect("../")
    else:
        print "no estoy recibiendo post, papo"
        return render(request, "comun/pacientes/presupuestos/registrar.html")


def presupuesto_pdf(request ,id_paciente ,id_presupuesto):
    presupuesto = Presupuesto.objects.get(pk = int(id_presupuesto))
    horarios = Horario.objects.filter(presupuesto = presupuesto)
    print horarios
    horas_semanales = 0
    for horario in horarios:
        horas_semanales += horario.cantidad_horas
    
    context = {
                'pagesize':'A4',
                'presupuesto':presupuesto,
                'horarios': horarios,
                'horas_semanales': horas_semanales,
                'horas_mensuales': horas_semanales*4,
                'costo_mensual': horas_semanales*4*presupuesto.costo_hora
              }
    
    print context
    presupuesto_pdf = render_to_pdf('comun/pacientes/presupuestos/pdf.html',context)
    #presupuesto_pdf = render(request, 'comun/pacientes/presupuestos/pdf.html',context)
    return presupuesto_pdf
    
    
"""
Funcion para renderizar un PDF
"""

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='aplication/pdf')
    return HttpResponse('Algo no salio bien <pre>%s</pre><br>Contacte al administrador o desarollador' % escape(html))

