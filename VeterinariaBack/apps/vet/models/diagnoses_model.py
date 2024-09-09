from django.db import models
from apps.vet.models.consults_model import Consults

class Diagnoses(models.Model):
    id = models.AutoField("Id", primary_key=True, db_column="id")
    detail = models.CharField("detail", max_length=255, null=True)
    date_diagnosis = models.DateField("date_diagnosis", null=True)
    consults = models.ForeignKey(Consults, models.DO_NOTHING,db_column='consult_id',null=False,blank=False)
    status = models.IntegerField("status", null=True)

    class Meta:
        verbose_name = "Diagnose"
        verbose_name_plural = "Diagnoses"
        db_table = "tbl_diagnoses"

    def __str__(self):
        return f"{self.id}{self.detail}"
