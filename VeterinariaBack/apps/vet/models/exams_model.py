from django.db import models
from apps.vet.models.consults_model import Consults

class Exams(models.Model):
    id = models.AutoField("IdExamen",primary_key=True,db_column="id")
    exam_date =models.DateTimeField("Fecha Examen",null=True)
    mucosa = models.CharField("mucosa",max_length=255,null=False)
    piel = models.CharField("piel",max_length=255,null=False)
    conjuntival = models.CharField("conjuntival",max_length=255,null=False)
    oral = models.CharField("oral",max_length=255,null=False)
    sis_reproductor = models.CharField("sis_reproductor",max_length=255,null=False)
    rectal = models.CharField("rectal",max_length=255,null=False)
    ojos = models.CharField("ojos",max_length=255,null=False)
    nodulos_linfaticos = models.CharField("nodulos_linfaticos",max_length=255,null=False)
    locomocion = models.CharField("locomocion",max_length=255,null=False)
    sis_cardiovascular = models.CharField("sis_cardiovascular",max_length=255,null=False)
    sis_respiratorio = models.CharField("sis_respiratorio",max_length=255,null=False)
    sis_digestivo = models.CharField("sis_digestivo",max_length=255,null=False)
    sis_urinario = models.CharField("sis_urinario",max_length=255,null=False)
    consults = models.ForeignKey(Consults,models.DO_NOTHING,db_column="id_consulta",blank=True,null=True)
    status = models.IntegerField("status",null=False)


    class Meta:
        verbose_name = "Examene"
        verbose_name_plural = "Examenes"
        db_table = "tbl_exams"

    def __str__(self):
        return f"{self.exam_date}"
