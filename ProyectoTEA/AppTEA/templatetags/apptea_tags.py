from django import template

register = template.Library()

@register.filter
def obtener_informes(paciente, area):
    return paciente.informe_set.filter(area=area)