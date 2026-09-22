from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .forms import ActivityForm, ContactForm
from .models import Activity


@login_required
def activity_list(request):
    activities = Activity.objects.all().order_by("-start_date")

    return render(
        request,
        "activities/activity_list.html",
        {"activities": activities},
    )

@login_required
def activity_create(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            activity = form.save(commit=False)
            activity.delegation = request.user.delegacion
            activity.responsible = request.user
            activity.save()

            return redirect("activities:list")
    else:
        form = ActivityForm()

    form.fields["delegation"].queryset = form.fields["delegation"].queryset.filter(
        id=request.user.delegacion_id
    )

    form.fields["responsible"].queryset = form.fields["responsible"].queryset.filter(
        id=request.user.id
    )

    return render(
        request,
        "activities/activity_new.html",
        {"form": form},
    )


@login_required
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    return render(
        request,
        "activities/activity_detail.html",
        {"activity": activity},
    )


@login_required
def activity_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)

        if form.is_valid():
            form.save()

            return redirect(
                "activities:detail",
                pk=activity.pk,
            )
    else:
        form = ActivityForm(instance=activity)

    return render(
        request,
        "activities/activity_form.html",
        {
            "form": form,
            "activity": activity,
        },
    )


@login_required
def contact_create(request):
    if request.method != "POST":
        return JsonResponse(
            {"success": False, "error": "Método no permitido."},
            status=405,
        )

    form = ContactForm(request.POST)

    if form.is_valid():
        contact = form.save()

        return JsonResponse({
            "success": True,
            "contact": {
                "id": contact.id,
                "name": contact.name,
            },
        })

    return JsonResponse(
        {
            "success": False,
            "errors": {
                field: errors.get_json_data()
                for field, errors in form.errors.items()
            },
        },
        status=400,
    )
