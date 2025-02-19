PATIENT_DATA = {
    "name": "Denis Vieira",
    "email": "denis@email.com",
    "address": "downtown",
    "gender": "male",
    "birth_date": "1990-01-01",
}

PATIENT_DATA_2 = {
    "name": "Denis Vieira 2",
    "email": "denis@email2.com",
    "address": "downtown 2",
    "gender": "other",
    "birth_date": "1999-01-01",
}


def generate_fhir(data):
    return {
        "resourceType": "Patient",
        "name": [
            {
                "use": "official",
                "text": data["name"],
            }
        ],
        "gender": data["gender"],
        "birthDate": data["birth_date"],
        "address": [
            {
                "type": "physical",
                "text": data["address"],
            }
        ],
        "telecom": [
            {
                "system": "email",
                "value": data["email"],
            },
        ],
    }


PATIENT_FHIR_DATA = generate_fhir(PATIENT_DATA)
PATIENT_FHIR_DATA_2 = generate_fhir(PATIENT_DATA_2)
