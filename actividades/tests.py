from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse

from accounts.models import Cargo, Delegacion, User
from .models import Activity, Contact


class PruebasIntegracionActividades(TestCase):
    """Pruebas de integración del módulo de actividades."""

    @classmethod
    def setUpTestData(cls):
        cls.delegacion = Delegacion.objects.create(
            nombre="Delegación de prueba",
            descripcion="Delegación para pruebas de integración.",
        )

        cls.usuario = User.objects.create_user(
            rut="12.345.678-9",
            password="Test1234!",
            first_name="Juan",
            last_name="Pérez",
            email="juan@example.com",
            delegacion=cls.delegacion,
        )

        cls.contacto = Contact.objects.create(
            name="Carlos González",
            phone="+56987654321",
            email="carlos@example.com",
            observations="Contacto de prueba.",
        )

    def setUp(self):
        self.client.force_login(self.usuario)

    def datos_actividad(self):
        return {
            "name": "Reunión de prueba",
            "description": "Solicitud de prueba de integración.",
            "action": "Coordinar reunión.",
            "item": "Gestión municipal",
            "contact": self.contacto.pk,
            "delegation": self.delegacion.pk,
            "responsible": self.usuario.pk,
            "start_date": "2026-10-08",
            "end_date": "",
            "status": Activity.Status.INGRESADO,
        }

    def test_creacion_integra_vista_formulario_modelo_y_bd(self):
        """La vista procesa el formulario y guarda la actividad y sus relaciones."""

        response = self.client.post(
            reverse("activities:create"),
            data=self.datos_actividad(),
        )

        self.assertEqual(
            response.status_code,
            302,
            "La creación válida debería redirigir después de guardar.",
        )

        actividad = Activity.objects.get(name="Reunión de prueba")

        self.assertEqual(actividad.responsible, self.usuario)
        self.assertEqual(actividad.delegation, self.delegacion)
        self.assertEqual(actividad.contact, self.contacto)

        self.assertIsNotNone(
            actividad.code,
            "La actividad debería tener un código UUID.",
        )

        self.assertEqual(
            Activity.objects.filter(code=actividad.code).count(),
            1,
            "El código debería identificar una sola actividad.",
        )

    def test_formulario_invalido_no_guarda_actividad(self):
        """Un formulario inválido no debe guardar una actividad."""

        datos = self.datos_actividad()
        datos["name"] = ""

        response = self.client.post(
            reverse("activities:create"),
            data=datos,
        )

        self.assertEqual(
            response.status_code,
            200,
            "El formulario inválido debería volver a mostrarse.",
        )

        self.assertFalse(
            Activity.objects.filter(
                description="Solicitud de prueba de integración."
            ).exists(),
            "No debería guardarse una actividad sin nombre.",
        )

    def test_usuario_no_autenticado_no_puede_crear_actividad(self):
        """Un usuario anónimo no puede acceder a la vista de creación."""

        self.client.logout()

        response = self.client.get(
            reverse("activities:create"),
        )

        self.assertEqual(
            response.status_code,
            302,
            "El usuario anónimo debería ser redirigido al inicio de sesión.",
        )

    def test_usuario_sin_permiso_no_puede_validar_actividades(self):
        """Un usuario sin permiso recibe una respuesta 403."""

        response = self.client.get(
            reverse("activities:validate"),
        )

        self.assertEqual(
            response.status_code,
            403,
            "El usuario sin permiso no debería acceder a la validación.",
        )

    def test_usuario_con_permiso_puede_validar_actividades(self):
        """Un usuario con permiso de validación puede acceder a la vista."""

        cargo = Cargo.objects.create(
            nombre="Verificador de prueba",
            descripcion="Cargo creado para pruebas.",
        )

        content_type = ContentType.objects.get_for_model(Activity)

        permiso, _ = Permission.objects.get_or_create(
            content_type=content_type,
            codename="validate_activities",
            defaults={
                "name": "Puede validar actividades",
            },
        )

        cargo.permisos.add(permiso)

        self.usuario.cargo = cargo
        self.usuario.save(update_fields=["cargo"])

        response = self.client.get(
            reverse("activities:validate"),
        )

        self.assertEqual(
            response.status_code,
            200,
            "El usuario con permiso debería acceder a la vista.",
        )