from django.contrib import admin

from .models import Actividad

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "delegacion",
        "fecha_inicio",
        "fecha_termino",
        "activa",
    )

    list_filter = (
        "delegacion",
        "activa",
    )

    search_fields = (
        "nombre",
        "descripcion",
    )

    ordering = (
        "fecha_inicio",
        "nombre",
    )