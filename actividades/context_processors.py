from django.urls import reverse


def dashboard_sidebar(request):
    if not request.user.is_authenticated:
        return {"sidebar_items": []}

    items = []

    if request.user.has_perm("actividades.manage_activities"):
        items.extend([
            {
                "label": "Actividades",
                "icon": "fa-solid fa-list-check",
                "url": reverse("activities:list"),
                "url_name": "list",
            },
            {
                "label": "Registrar actividad",
                "icon": "fa-solid fa-plus",
                "url": reverse("activities:create"),
                "url_name": "create",
            },
        ])

    if request.user.has_perm("actividades.validate_activities"):
        items.append({
            "label": "Validar actividades",
            "icon": "fa-solid fa-circle-check",
            "url": reverse("activities:validate"),
            "url_name": "validate",
        })

    return {"sidebar_items": items}