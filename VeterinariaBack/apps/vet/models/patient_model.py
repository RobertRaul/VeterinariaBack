from django.db import models
from apps.vet.models.client_model import Client
from apps.vet.models.breed_model import Breed


# Create your models here.
# TBL_PATIENTS
class Patient(models.Model):
    id = models.AutoField("IdCargo", primary_key=True, db_column="id")
    names = models.CharField("names", max_length=255, null=False)
    photo = models.CharField("photo", max_length=255, null=False)
    birthday = models.DateField("birthday", null=True)
    age = models.CharField("age", max_length=10, null=False)
    sex = models.CharField("sex", max_length=1, null=False)
    color = models.CharField("color", max_length=255, null=False)
    fur = models.CharField("fur", max_length=255, null=False)
    particularity = models.CharField("particularity", max_length=255, null=False)
    allergy = models.CharField("allergy", max_length=255, null=False)
    breed = models.ForeignKey(
        Breed, models.DO_NOTHING, db_column="breed_id", blank=False, null=False
    )
    client = models.ForeignKey(
        Client, models.DO_NOTHING, db_column="client_id", blank=False, null=False
    )
    status = models.IntegerField("allergy", null=False)
    public_id = models.CharField("public_id", max_length=255, null=False)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        db_table = "tbl_patients"

    def __str__(self):
        return f"{self.names} {self.color}"
