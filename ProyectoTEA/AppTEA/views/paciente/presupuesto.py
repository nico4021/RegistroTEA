# -*- coding: utf-8 -*-

from AppTEA.views import *


"""
Vista que muestra la lista de presupuestos de distintas fechas 
de un paciente específico.

Recibe como parámetro el id del paciente.
"""
@login_required(login_url="/loguearse")
def presupuestos(request, id_paciente):
    # Obtengo el paciente
    paciente = Paciente.objects.get(pk=id_paciente)
    presupuestos = Presupuesto.objects.filter(paciente = paciente.pk).filter(is_active = True).order_by("fecha_creacion")
    context = {"presupuestos": presupuestos,
                   "btn_enlace": "agregar/",
                   "btn_icono": "add" }
    template = render(request, "comun/pacientes/presupuestos/index.html", context)        
    return template

def presupuesto_pdf(request ,id_paciente ,id_presupuesto):
    presupuesto = Presupuesto.objects.get(pk = id_presupuesto)
    context = {
                'pagesize':'A4',
                'presupuesto':presupuesto
              }
    presupuesto_pdf = render_to_pdf('comun/pacientes/presupuestos/pdf.html',context)
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

def registrar(request, id_paciente):
    return render(request, "comun/pacientes/presupuestos/registrar.html")