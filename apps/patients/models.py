from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from fhir.resources.patient import Patient as FhirPatient


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    birth_date = models.DateField()
    address = models.TextField()
    gender = models.CharField(
        max_length=25,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
            ("unknown", "Unknown"),
        ],
    )

    def clean(self):
        """Valida se os dados podem ser convertidos corretamente para FHIR"""
        try:
            self.to_fhir()
        except Exception as e:
            raise ValidationError(f"Invalid FHIR Data: {str(e)}")

        if not self.name:
            raise ValidationError("Name is required")

        if not self.email:
            raise ValidationError("Email is required")

        if not self.birth_date:
            raise ValidationError("Birth Date is required")

        if not self.address:
            raise ValidationError("Address is required")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def to_fhir(self):
        fhir_patient = FhirPatient(
            **{
                "resourceType": "Patient",
                "id": str(self.id),
                "name": [
                    {
                        "use": "official",
                        "text": self.name,
                    }
                ],
                "gender": self.gender,
                "birthDate": str(self.birth_date),
                "address": [
                    {
                        "type": "physical",
                        "text": self.address,
                    }
                ],
                "telecom": [
                    {
                        "system": "email",
                        "value": self.email,
                    },
                ],
            }
        )
        return fhir_patient

    @classmethod
    def from_fhir(cls, fhir_data):
        instance = cls()
        instance.fill_data_from_fhir(fhir_data)
        return instance

    def fill_data_from_fhir(self, fhir_data):
        try:
            FhirPatient(**fhir_data)
        except Exception as e:
            raise ValidationError(f"Invalid FHIR Data: {str(e)}")

        if fhir_data.get("name") and (name := fhir_data["name"][0].get("text")):
            self.name = name

        if fhir_data.get("telecom") and (email := fhir_data["telecom"][0].get("value")):
            self.email = email

        if gender := fhir_data.get("gender"):
            self.gender = gender

        if birth_date := fhir_data.get("birthDate"):
            self.birth_date = birth_date

        if fhir_data.get("address") and (
            address := fhir_data["address"][0].get("text")
        ):
            self.address = address

    def __str__(self):
        return self.name
