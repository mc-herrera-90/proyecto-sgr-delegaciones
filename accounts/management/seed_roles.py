from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

ROLES = [
    "Administrador",
    "Coordinador",
    "Delegado",
    "Funcionario",
    "Verificador",
    "Consulta",
]

class Command(BaseCommand):
    help = "Crea roles base (Groups) del sistema SGR"

    def handle(self, *args, **kwargs):
        for name in ROLES:
            Group.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Roles creados/actualizados."))