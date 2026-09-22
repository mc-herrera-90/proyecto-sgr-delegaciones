from django.urls import path

from . import views

app_name = "activities"

urlpatterns = [
    path("", views.activity_list, name="list"),
    path("create/", views.activity_create, name="create"),
    path("<int:pk>/", views.activity_detail, name="detail"),
    path("<int:pk>/edit/", views.activity_update, name="update"),
    path("contacts/create/", views.contact_create, name="contact_create")
]