from django import forms

from .models import Activity, Contact


class ActivityForm(forms.ModelForm):

    contact = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        empty_label="Seleccione una opción",
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    class Meta:
        model = Activity
        fields = [
            "name",
            "description",
            "action",
            "item",
            "contact",
            "delegation",
            "responsible",
            "start_date",
            "end_date",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre de la actividad",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descripción de la solicitud o problema",
                }
            ),
            "action": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Acción realizada o por realizar",
                }
            ),
            "item": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ítem relacionado",
                }
            ),
            "contact": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "delegation": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "responsible": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "phone",
            "email",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del contacto",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Teléfono",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Correo electrónico",
                }
            ),
            "observations": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Información adicional del contacto",
                }
            ),
        }
