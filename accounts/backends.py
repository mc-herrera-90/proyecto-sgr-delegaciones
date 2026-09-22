from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class RUTBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        rut = kwargs.get("rut", username)

        if not rut or not password:
            return None

        try:
            user = User.objects.get(rut=rut)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None


class CargoPermissionBackend(ModelBackend):

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous:
            return set()

        permissions = super().get_all_permissions(user_obj, obj)

        if not user_obj.cargo:
            return permissions

        cargo_permissions = user_obj.cargo.permisos.values_list(
            "content_type__app_label",
            "codename",
        )

        permissions.update(
            f"{app_label}.{codename}"
            for app_label, codename in cargo_permissions
        )

        return permissions