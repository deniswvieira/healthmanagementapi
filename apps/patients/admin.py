from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gender", "birth_date", "email")
    search_fields = ("name", "gender", "email")
    list_filter = ("gender",)
