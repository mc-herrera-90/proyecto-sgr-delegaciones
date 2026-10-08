from django.contrib.auth import authenticate
from django.test import TestCase

from .models import User


class PruebasAutenticacion(TestCase):
    """Pruebas del sistema de autenticación mediante RUT y contraseña."""

    @classmethod
    def setUpTestData(cls):
        cls.usuario = User.objects.create_user(
            rut="12.345.678-9",
            password="Test1234!",
            first_name="Juan",
            last_name="Pérez",
            email="juan.perez@example.com",
        )

    def test_autenticacion_acepta_credenciales_validas(self):
        """El usuario puede ingresar con sus credenciales correctas."""

        usuario = authenticate(
            rut="12.345.678-9",
            password="Test1234!",
        )

        self.assertIsNotNone(
            usuario,
            "ERROR: se esperaba autenticar al usuario con credenciales válidas.",
        )
        self.assertEqual(usuario, self.usuario)
        self.assertTrue(usuario.is_authenticated)

    def test_autenticacion_rechaza_contrasena_incorrecta(self):
        """Se rechaza el acceso cuando la contraseña es incorrecta."""

        usuario = authenticate(
            rut="12.345.678-9",
            password="ContrasenaIncorrecta!",
        )

        self.assertIsNone(
            usuario,
            "ERROR: se autenticó un usuario con una contraseña incorrecta.",
        )

    def test_autenticacion_rechaza_rut_inexistente(self):
        """Se rechaza el acceso cuando el RUT no está registrado."""

        usuario = authenticate(
            rut="11.111.111-1",
            password="Test1234!",
        )

        self.assertIsNone(
            usuario,
            "ERROR: se autenticó un RUT que no existe.",
        )

    def test_autenticacion_rechaza_contrasena_vacia(self):
        """Se rechaza el acceso si no se proporciona contraseña."""

        usuario = authenticate(
            rut="12.345.678-9",
            password="",
        )

        self.assertIsNone(
            usuario,
            "ERROR: se permitió autenticar sin contraseña.",
        )

    def test_usuario_inactivo_no_puede_autenticarse(self):
        """Un usuario deshabilitado no puede ingresar al sistema."""

        self.usuario.is_active = False
        self.usuario.save(update_fields=["is_active"])

        usuario = authenticate(
            rut="12.345.678-9",
            password="Test1234!",
        )

        self.assertIsNone(
            usuario,
            "ERROR: se permitió el acceso a un usuario inactivo.",
        )

    def test_contrasena_se_almacena_con_hash(self):
        """La contraseña se almacena mediante un hash, no como texto plano."""

        self.assertNotEqual(
            self.usuario.password,
            "Test1234!",
            "ERROR: la contraseña parece estar almacenada como texto plano.",
        )

        self.assertTrue(
            self.usuario.check_password("Test1234!"),
            "ERROR: Django no pudo verificar la contraseña almacenada.",
        )