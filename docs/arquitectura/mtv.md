# Patrón MTV

Django utiliza una arquitectura basada en el patrón
**Model-Template-View (MTV)**, que permite separar la representación
de los datos, la interfaz de usuario y la lógica de procesamiento.

## Model

El **Model** representa la estructura de los datos de la aplicación.

En Django, los modelos se definen mediante clases que heredan de
`django.db.models.Model`.

Por ejemplo, el modelo de usuario personalizado del sistema:

```python
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    rut = models.CharField(
        max_length=12,
        unique=True,
    )

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []