from django.contrib import admin
from .models import Profesional, Presupuesto, Paciente, Area, Horario

# Register your models here.
admin.site.register(Horario)
admin.site.register(Profesional)
admin.site.register(Presupuesto)
admin.site.register(Paciente)
admin.site.register(Area)