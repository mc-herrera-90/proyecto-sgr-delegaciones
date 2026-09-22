from django.contrib import admin

from .models import Activity, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact",
        "delegation",
        "responsible",
        "start_date",
        "status",
    )

    list_filter = (
        "delegation",
        "status",
    )

    search_fields = (
        "name",
        "description",
        "action",
        "item",
        "contact__name",
        "responsible__first_name",
        "responsible__last_name",
    )

    ordering = (
        "start_date",
        "name",
    )
