import pytest
from django.core.exceptions import ValidationError

from apps.patients.models import Patient

from .definitions import PATIENT_DATA, PATIENT_FHIR_DATA


@pytest.fixture
def patient():
    return Patient.objects.create(
        name="Denis Vieira",
        email="denis@email.com",
        address="downtown",
        gender="male",
        birth_date="1980-01-01",
    )


@pytest.mark.django_db
def test_patient_model_creation():
    patient = Patient.objects.create(**PATIENT_DATA)
    assert patient.id is not None


@pytest.mark.django_db
def test_patient_empty():
    patient = Patient()

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_without_name():
    patient = Patient(
        **{key: val for key, val in PATIENT_DATA.items() if key != "name"}
    )

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_without_email():
    patient = Patient(
        **{key: val for key, val in PATIENT_DATA.items() if key != "email"}
    )

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_without_gender():
    patient = Patient(
        **{key: val for key, val in PATIENT_DATA.items() if key != "gender"}
    )

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_without_birth_date():
    patient = Patient(
        **{key: val for key, val in PATIENT_DATA.items() if key != "birth_date"}
    )

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_without_address():
    patient = Patient(
        **{key: val for key, val in PATIENT_DATA.items() if key != "address"}
    )

    with pytest.raises(ValidationError):
        patient.save()


@pytest.mark.django_db
def test_patient_to_fhir(patient):
    fhir_patient = patient.to_fhir().model_dump()
    assert fhir_patient["resourceType"] == "Patient"
    assert fhir_patient["id"] == str(patient.id)
    assert fhir_patient["name"][0]["text"] == patient.name
    assert fhir_patient["telecom"][0]["value"] == patient.email
    assert fhir_patient["gender"] == patient.gender
    assert fhir_patient["birthDate"] == patient.birth_date
    assert fhir_patient["address"][0]["text"] == patient.address


@pytest.mark.django_db
def test_patient_from_fhir():
    patient = Patient.from_fhir(PATIENT_FHIR_DATA)
    assert patient.name == PATIENT_DATA["name"]
    assert patient.email == PATIENT_DATA["email"]
    assert patient.gender == PATIENT_DATA["gender"]
    assert patient.address == PATIENT_DATA["address"]
    assert str(patient.birth_date) == PATIENT_DATA["birth_date"]
