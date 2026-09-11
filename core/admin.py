from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("rut",)
    list_display = ("rut", "nombre", "apellido_paterno", "cargo", "is_active", "is_staff")
    search_fields = ("rut", "nombre", "apellido_paterno", "email")

    fieldsets = (
        (None, {"fields": ("rut", "password")}),
        (
            "Información personal",
            {
                "fields": (
                    "nombre",
                    "apellido_paterno",
                    "apellido_materno",
                    "email",
                    "telefono",
                    "direccion",
                )
            },
        ),
        (
            "Información laboral",
            {"fields": ("departamento", "cargo", "fecha_ingreso")},
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("rut", "password1", "password2"),
            },
        ),
    )