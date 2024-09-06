from django.db import models
from apps.vet.models.specie_model import Specie


class Breed(models.Model):
    id = models.AutoField("Id", primary_key=True, db_column="id")
    name = models.CharField("name", max_length=100, null=False)
    status = models.IntegerField("status", null=True)
    specie = models.ForeignKey(
        Specie, models.DO_NOTHING, db_column="specie_id", blank=False, null=False
    )

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"
        db_table = "tbl_breeds"

    def __str__(self):
        return f"{self.name}"
