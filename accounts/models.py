from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class Delegacion(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Delegación"
        verbose_name_plural = "Delegaciones"

    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nombre
    
class User(AbstractUser):
    username = None
    rut = models.CharField(max_length=12, unique=True) # para formatos 12.245.678-9
    email = models.EmailField(unique=True, blank=True, null=True)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    delegacion = models.ForeignKey(
        Delegacion,
        on_delete=models.PROTECT,
        related_name="usuarios",
        null=True,
        blank=True
    )

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT,
        related_name="usuarios",
        null=True,
        blank=True,
    )