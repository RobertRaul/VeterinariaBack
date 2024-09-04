from django.db import models

# Create your models here.

class Cargo(models.Model):
    IdCargo = models.AutoField("IdCargo", primary_key=True)
    NombreCargo = models.CharField("Descripcion del Cargo", max_length=50, null=False)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        db_table = 'Cargo'


class Ubigeo(models.Model):
    IdUbigeo = models.AutoField("IdUbigeo", primary_key=True)
    Ubigeo = models.CharField("Ubigeo", max_length=50, null=True)
    Distrito = models.CharField("Distrito", max_length=255, null=True)
    Provincia = models.CharField("Provincia", max_length=255, null=True)
    Departamento = models.CharField("Departamento", max_length=255, null=True)
    Ubicacion = models.CharField("Ubicacion", max_length=255, null=True)

    class Meta:
        verbose_name = "Ubigeo"
        verbose_name_plural = "Ubigeos"
        db_table = 'Ubigeo'

    def __str__(self):
        return self.Ubigeo


class Empleado(models.Model):
    IdCargo = models.AutoField("IdEmpleado", primary_key=True)
    TipoDoc = models.CharField("TipoDoc", max_length=30, null=False)
    NroDoc = models.CharField("NroDoc", max_length=15, null=False)
    NombreCompleto = models.CharField("NombreCompleto", max_length=255, null=False)
    FechaNac = models.DateField("FechaNac", null=False)
    Direccion = models.CharField("Direccion", max_length=30, null=False)
    IdUbigeo = models.ForeignKey(
        Ubigeo, on_delete=models.CASCADE, verbose_name="Ubigeo"
    )
    Email = models.CharField("Email", max_length=100, null=False)
    Telefono = models.CharField("Telefono", max_length=15, null=False)
    IdCargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name="Cargo")
    Estado = models.BooleanField("Estado", default=True)
    FechaCreacion = models.DateField("FechaCreacion", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = 'Empleado'