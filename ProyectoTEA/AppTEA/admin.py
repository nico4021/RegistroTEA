from django.contrib import admin
from .models import Profesional, Presupuesto, Paciente, Area

# Register your models here.
admin.site.register(Profesional)
admin.site.register(Presupuesto)
admin.site.register(Paciente)
admin.site.register(Area)