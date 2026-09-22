from django.contrib.auth.views import LoginView
from django.urls import reverse


class SGRLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse("admin:index")

        if self.request.user.has_perm("actividades.manage_activities"):
            return reverse("activities:list")

        return reverse("core:dashboard")