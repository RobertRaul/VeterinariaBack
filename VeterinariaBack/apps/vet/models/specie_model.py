from django.db import models


class Specie(models.Model):
    id = models.AutoField("Id", primary_key=True, db_column="id")
    name = models.CharField("name", max_length=50, null=True)
    scientificName = models.CharField("status", max_length=100, null=True)
    status = models.IntegerField("specie_id", null=True)

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"
        db_table = "tbl_species"

    def __str__(self):
        return f"{self.id}{self.name}"
