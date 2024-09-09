from django.db import models
from apps.vet.models.patient_model import Patient

class Recetas(models.Model):
    id=models.AutoField("Id",primary_key=True,db_column="id")
    description=models.CharField('description',max_length=255,null=True)
    indicaciones=models.CharField('Descripcion',max_length=255,null=True)
    created_at =models.DateField('Fecha registro',null=True)
    patient=models.ForeignKey(Patient,models.DO_NOTHING,db_column="patient_id",blank=True,null=True)
    status=models.IntegerField('Descripcion',null=True)

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"        
        ordering = ["id"]
        db_table = "tbl_recetas"  
        

    def __str__(self):
        return f"{self.description}"

    

