from django.contrib.auth.views import LoginView
from django.urls import reverse


class SGRLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("admin:index")

        return reverse("core:dashboard")
