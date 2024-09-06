from django.db import models


# Create your models here.
# TBL_CLIENTS
class Client(models.Model):
    Id = models.AutoField("IdCargo", primary_key=True, db_column="id")
    photo = models.CharField("photo", max_length=255, null=False)
    names = models.CharField("names", max_length=255, null=False)
    lastnames = models.CharField("lastnames", max_length=255, null=False)
    document_type = models.CharField("document_type", max_length=30, null=False)
    document_number = models.CharField("document_number", max_length=15, null=False)
    address = models.CharField("address", max_length=255, null=True)
    city = models.CharField("city", max_length=255, null=True)
    email = models.CharField("email", max_length=255, null=True)
    phone = models.CharField("phone", max_length=15, null=True)
    status = models.IntegerField("status", null=True)
    # registrationDate = models.DateTimeField("registrationDate",null=True)
    # idEmployeeCreates = models.IntegerField("idEmployeeCreates", max_length=255,null=True)
    # modifiedDate = models.DateTimeField("modifiedDate",null=True)
    # idEmployeeModifies = models.IntegerField("idEmployeeModifies", max_length=255,null=True)
    # deletedDate = models.DateTimeField("deletedDate",null=True)
    # idEmployeeDeletes = models.IntegerField("idEmployeeDeletes", max_length=255,null=True)
    public_id = models.CharField("public_id", max_length=255, null=True)
    password = models.CharField("password", max_length=255, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "tbl_clients"

    def __str__(self):
        return f"{self.lastnames} {self.email}"
