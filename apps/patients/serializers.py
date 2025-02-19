from django.core.exceptions import ValidationError
from fhir.resources.patient import Patient as FhirPatient
from rest_framework import serializers

from .models import Patient
from .schemas import FHIR_FULL_PATIENT_SCHEMA
from .utils import clean_object_with_openapi_schema


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = []

    def to_internal_value(self, data):
        # bypass the convertion to python types
        if not data:
            raise serializers.ValidationError("No data provided")
        return data

    def validate(self, attrs):
        try:
            print("validating", attrs)
            FhirPatient(**attrs)
        except Exception as e:
            raise serializers.ValidationError(f"Invalid FHIR Data: {str(e)}")
        return attrs

    def create(self, validated_data):
        try:
            patient = Patient.from_fhir(validated_data)
            patient.save()
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return patient

    def update(self, patient, validated_data):
        try:
            patient.fill_data_from_fhir(validated_data)
            patient.save()
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return patient

    def to_representation(self, instance):
        return clean_object_with_openapi_schema(
            instance.to_fhir().model_dump(), FHIR_FULL_PATIENT_SCHEMA
        )
