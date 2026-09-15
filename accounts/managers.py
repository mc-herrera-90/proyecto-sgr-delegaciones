from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):

    def create_user(self, rut, email=None, password=None, **extra_fields):
        if not rut:
            raise ValueError("El RUT es obligatorio")

        user = self.model(
            rut=rut,
            email=email,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, rut, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(
            rut=rut,
            email=email,
            password=password,
            **extra_fields,
        )