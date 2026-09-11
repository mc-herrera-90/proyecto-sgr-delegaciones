from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class RutAuthenticationForm(AuthenticationForm):
    """
    Formulario de login basado en AuthenticationForm de Django.

    - El campo "username" se mapea automáticamente al USERNAME_FIELD
      del modelo de usuario personalizado (definido en la tarea N°1,
      se asume USERNAME_FIELD = "rut").
    - Se sobreescribe el mensaje de error para no revelar si el RUT
      existe o no en el sistema (mensaje 100% genérico).
    """

    error_messages = {
        "invalid_login": _(
            "Credenciales inválidas. Verifica tu RUT y contraseña e "
            "inténtalo nuevamente."
        ),
        "inactive": _("Esta cuenta se encuentra inactiva."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "RUT"
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Ej: 12345678-9",
                "autofocus": True,
                "autocomplete": "username",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "••••••••",
                "autocomplete": "current-password",
            }
        )