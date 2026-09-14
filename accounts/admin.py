from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

    def has_module_permission(self, request):
        return False

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
                "delegacion",
            ),
        }),
        ("Permisos", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
        }),
    )

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