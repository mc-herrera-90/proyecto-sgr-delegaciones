from django.db import models

from accounts.models import Delegacion, User


class Actividad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    delegacion = models.ForeignKey(
        Delegacion,
        on_delete=models.PROTECT,
        related_name="actividades",
    )

    responsable = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="actividades_responsables",
    )

    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(null=True, blank=True)

    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ("fecha_inicio", "nombre")

    def __str__(self):
        return self.nombre