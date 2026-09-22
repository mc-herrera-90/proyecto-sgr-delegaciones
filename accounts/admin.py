from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .models import User, Delegacion, Cargo


@admin.register(Delegacion)
class DelegacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activa")
    list_filter = ("activa",)
    search_fields = ("nombre",)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        form.base_fields["permisos"].queryset = Permission.objects.filter(
            content_type__app_label="actividades",
            codename__in=[
                "manage_activities",
                "validate_activities",
            ],
        )

        return form


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "rut",
        "email",
        "first_name",
        "last_name",
        "cargo",
        "delegacion",
        "is_active",
    )

    list_filter = (
        "cargo",
        "delegacion",
        "is_active",
    )

    search_fields = (
        "rut",
        "email",
        "first_name",
        "last_name",
    )

    ordering = ("rut",)

    fieldsets = (
        (None, {
            "fields": ("rut", "password"),
        }),
        ("Información del usuario", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "cargo",
                "delegacion",
            ),
        }),
        ("Estado", {
            "fields": (
                "is_active",
            ),
        }),
        ("Permisos del cargo", {
            "fields": (
                "mostrar_permisos_cargo",
            ),
        }),
    )

    readonly_fields = (
        "mostrar_permisos_cargo",
    )

    def mostrar_permisos_cargo(self, obj):
        if not obj or not obj.cargo:
            return "Sin cargo asignado."

        permisos = obj.cargo.permisos.all()

        if not permisos.exists():
            return "El cargo no tiene permisos asignados."

        return ", ".join(
            permiso.name for permiso in permisos
        )

    mostrar_permisos_cargo.short_description = "Permisos asignados"

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "rut",
                "first_name",
                "last_name",
                "email",
                "cargo",
                "delegacion",
                "password1",
                "password2",
                "is_active",
            ),
        }),
    )