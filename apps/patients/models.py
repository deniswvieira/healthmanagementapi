from django.core.validators import EmailValidator
from django.db import models


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=25,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
            ("unknown", "Unknown"),
        ],
    )
    birth_date = models.DateField()
    address = models.TextField()
    email = models.EmailField(validators=[EmailValidator()])
