from drf_yasg import openapi

RESOURCE_TYPE = openapi.Schema(type=openapi.TYPE_STRING, example="Patient")

ID = openapi.Schema(type=openapi.TYPE_STRING, example="7")

NAME = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "use": openapi.Schema(type=openapi.TYPE_STRING, example="official"),
            "text": openapi.Schema(type=openapi.TYPE_STRING, example="Mark Smith"),
        },
    ),
)

GENDER = openapi.Schema(type=openapi.TYPE_STRING, example="male")

BIRTH_DATE = openapi.Schema(
    type=openapi.TYPE_STRING,
    format="date",
    example="1971-01-01",
)

ADDRESS = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="10 Side Street, Zurich, Switzerland",
            ),
        },
    ),
)


TELECOM = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "system": openapi.Schema(type=openapi.TYPE_STRING, example="email"),
            "value": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="mark@smith.com",
            ),
        },
    ),
)

BASE_PATIENT_PROPERTIES = {
    "resourceType": RESOURCE_TYPE,
    "name": NAME,
    "gender": GENDER,
    "birthDate": BIRTH_DATE,
    "address": ADDRESS,
    "telecom": TELECOM,
}

FULL_PATIENT_PROPERTIES = {
    **BASE_PATIENT_PROPERTIES,
    "id": ID,
}

FHIR_BASE_PATIENT_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        **BASE_PATIENT_PROPERTIES,
    },
)

FHIR_FULL_PATIENT_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        **FULL_PATIENT_PROPERTIES,
    },
)
