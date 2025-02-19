import pytest

from apps.patients.serializers import PatientSerializer

from .definitions import PATIENT_FHIR_DATA


@pytest.mark.django_db
def test_valid_patient_serializer():
    serializer = PatientSerializer(data=PATIENT_FHIR_DATA)
    assert serializer.is_valid()
    assert serializer.validated_data == PATIENT_FHIR_DATA


@pytest.mark.django_db
def test_invalid_patient_serializer():
    serializer = PatientSerializer(data={"hello": "world"})
    assert not serializer.is_valid()
