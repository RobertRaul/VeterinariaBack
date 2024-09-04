from django.db import models
from apps.empleados.models import Ubigeo


# Create your models here.
class Clientes(models.Model):
    IdCliente = models.AutoField("IdCargo", primary_key=True)
    TipoDoc = models.CharField("Tipo Documento", max_length=30, null=False)
    NroDoc = models.CharField("Numero Documento", max_length=15, null=False)
    NombreCompleto = models.CharField("NombreCompleto   ", max_length=255, null=False)
    FechaNac = models.DateField("FechaNac Nacimiento", null=False)
    Direccion = models.CharField("Direccion ", max_length=255, null=False)
    IdUbigeo = models.ForeignKey(
        Ubigeo, on_delete=models.CASCADE, verbose_name="Ubigeo", db_column="IdUbigeo"
    )
    email = models.CharField("Email", max_length=100, null=False)
    password = models.CharField("password", max_length=20, null=True)
    Telefono = models.CharField("Telefono", max_length=15, null=False)
    Estado = models.BooleanField("Estado", default=True)
    UsuarioCrea = models.IntegerField("UsuarioCrea", null=True,blank=True)
    FechaCreacion = models.DateTimeField("FechaCreacion", null=True)
    UsuarioModifica = models.IntegerField("UsuarioModifica", null=True)
    FechaModificado = models.DateTimeField("FechaModificado", null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "Cliente"

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    
    def __str__(self):        
        return f'{self.NombreCompleto} {self.email}'