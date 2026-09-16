from django.urls import path

from .views import SGRLoginView

app_name = "accounts"

urlpatterns = [
    path("login/", SGRLoginView.as_view(), name="login"),
]
