import datetime

from django.contrib import admin
from django.utils import timezone

from .models import Equipo
from.models import Profesor
from.models import Turno


class TurnoInline(admin.TabularInline):
    model = Turno

    def get_queryset(self, request):
        qs = super(TurnoInline, self).get_queryset(request)

        return qs.filter(fecha_inicio__gte=timezone.now())


class EquipoAdmin(admin.ModelAdmin):
    inlines = [TurnoInline]


class ProfesorAdmin(admin.ModelAdmin):
    inlines = [TurnoInline]


class TurnoAdmin(admin.ModelAdmin):
    list_display = ("fecha_inicio", "fecha_fin", "referencia_equipo", "referencia_profesor")


admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Turno, TurnoAdmin)
admin.site.index_title = "Sistema de Cañones"
admin.site.site_title = "Sistema de Cañones"
admin.site.site_header = "Prueba"