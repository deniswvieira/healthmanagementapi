import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from apps.patients.models import Patient

from .definitions import (
    PATIENT_DATA,
    PATIENT_DATA_2,
    PATIENT_FHIR_DATA,
    PATIENT_FHIR_DATA_2,
)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    return User.objects.create_user(username="testuser", password="testpassword")


@pytest.fixture
def auth_client(api_client, create_user):
    response = api_client.post(
        "/api/token/",
        {"username": "testuser", "password": "testpassword"},
        format="json",
    )
    token = response.data.get("access")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture
def patient():
    return Patient.objects.create(**PATIENT_DATA)


@pytest.mark.django_db
def test_create_patient(auth_client):
    response = auth_client.post("/fhir/patient/", PATIENT_FHIR_DATA, format="json")
    assert response.status_code == 201
    assert response.data["resourceType"] == "Patient"


@pytest.mark.django_db
def test_invalid_patient_creation(auth_client):
    response = auth_client.post("/fhir/patient/", PATIENT_DATA, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_patient_list(auth_client):
    Patient.objects.create(**PATIENT_DATA)
    response = auth_client.get("/fhir/patient/")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_update_patient(auth_client, patient):
    url = f"/fhir/patient/{patient.id}/"
    response = auth_client.put(url, PATIENT_FHIR_DATA_2, format="json")

    assert response.status_code == 200
    assert response.data["name"][0]["text"] == PATIENT_DATA_2["name"]
    assert response.data["gender"] == PATIENT_DATA_2["gender"]
    assert str(response.data["birthDate"]) == PATIENT_DATA_2["birth_date"]
    assert response.data["address"][0]["text"] == PATIENT_DATA_2["address"]
    assert response.data["telecom"][0]["value"] == PATIENT_DATA_2["email"]
    assert response.data["id"] == str(patient.id)


@pytest.mark.django_db
def test_update_patient_invalid(auth_client, patient):
    url = f"/fhir/patient/{patient.id}/"
    response = auth_client.put(url, {"hello": "world"}, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_partial_update_patient(auth_client, patient):
    url = f"/fhir/patient/{patient.id}/"
    assert patient.gender == PATIENT_DATA["gender"]
    response = auth_client.patch(url, {"gender": "unknown"}, format="json")
    assert response.status_code == 200
    assert response.data["gender"] == "unknown"


@pytest.mark.django_db
def test_partial_update_patient_invalid(auth_client, patient):
    url = f"/fhir/patient/{patient.id}/"
    response = auth_client.patch(url, {"hello": "workd"}, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_patient(auth_client, patient):
    url = f"/fhir/patient/{patient.id}/"
    response = auth_client.delete(url)
    assert response.status_code == 204
    assert Patient.objects.count() == 0


@pytest.mark.django_db
def test_delete_patient_invalid(auth_client):
    url = "/fhir/patient/123/"
    response = auth_client.delete(url)
    assert response.status_code == 404
    assert Patient.objects.count() == 0
