from fhir.resources.patient import Patient as FHIRPatient
from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def validate(self, data):
        fhir_patient = FHIRPatient(**data)
        try:
            fhir_patient.model_validate()
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return data
