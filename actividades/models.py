from django.db import models

from accounts.models import Delegacion, User


class Contact(models.Model):
    name = models.CharField("Nombre", max_length=200)
    phone = models.CharField("Teléfono", max_length=20)
    email = models.EmailField("Correo", blank=True)
    observations = models.TextField( "Observaciones", blank=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.name


class Activity(models.Model):
    class Status(models.TextChoices):
        INGRESADO = "INGRESADO", "Ingresado"
        PENDIENTE = "PENDIENTE", "Pendiente"
        EN_PROCESO = "EN_PROCESO", "En proceso"
        REALIZADO = "REALIZADO", "Realizado"

    name = models.CharField("Actividad", max_length=200)
    description = models.TextField("Solicitud / problema", blank=True)
    action = models.TextField("Acción", blank=True)
    item = models.CharField("Ítem", max_length=200, blank=True)

    contact = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        related_name="activities",
        verbose_name="Contacto",
        null=True
    )

    delegation = models.ForeignKey(
        Delegacion,
        on_delete=models.PROTECT,
        related_name="activities",
        verbose_name="Delegación",
    )

    responsible = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="responsible_activities",
        verbose_name="Responsable",
    )

    start_date = models.DateField("Fecha")
    end_date = models.DateField(
        "Fecha de término",
        null=True,
        blank=True,
    )

    status = models.CharField(
        "Estado",
        max_length=20,
        choices=Status.choices,
        default=Status.INGRESADO,
    )

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ("start_date", "name")

    def __str__(self):
        return self.name
