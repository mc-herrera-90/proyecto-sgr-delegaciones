from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado del SGR (Sistema de Gestión de
    Resultados), usando RUT como identificador de login (USERNAME_FIELD),
    en lugar del username por defecto de Django.
    """

    rut = models.CharField(
        "RUT",
        max_length=12,
        unique=True,
        help_text="Formato: 12345678-9",
    )
    nombre = models.CharField("Nombre", max_length=100, blank=True)
    apellido_paterno = models.CharField(
        "Apellido paterno", max_length=100, blank=True
    )
    apellido_materno = models.CharField(
        "Apellido materno", max_length=100, blank=True
    )
    email = models.EmailField("Correo electrónico", blank=True)
    telefono = models.CharField("Teléfono", max_length=20, blank=True)
    direccion = models.CharField("Dirección", max_length=255, blank=True)
    departamento = models.CharField("Departamento", max_length=100, blank=True)
    cargo = models.CharField("Cargo", max_length=100, blank=True)
    fecha_ingreso = models.DateField("Fecha de ingreso", null=True, blank=True)

    is_active = models.BooleanField("Activo", default=True)
    is_staff = models.BooleanField("Acceso al admin", default=False)
    date_joined = models.DateTimeField("Fecha de creación", auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []  # rut + password son suficientes para createsuperuser

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido_paterno}".strip()

    def get_full_name(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}".strip()

    def get_short_name(self):
        return self.nombre or self.rut