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