from django.contrib import admin
from admin_interface.admin import Theme
# Register your models here.

admin.site.unregister(Theme)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    fields = (
        "logo",
        "favicon",
    )