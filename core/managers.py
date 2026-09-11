from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager para el modelo User personalizado, que usa "rut" en vez de
    "username" como identificador único (USERNAME_FIELD).
    """

    use_in_migrations = True

    def _create_user(self, rut, password, **extra_fields):
        if not rut:
            raise ValueError("El usuario debe tener un RUT.")
        rut = rut.strip()
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, rut, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(rut, password, **extra_fields)

    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self._create_user(rut, password, **extra_fields)