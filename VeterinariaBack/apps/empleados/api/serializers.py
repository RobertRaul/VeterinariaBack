from rest_framework import serializers
from apps.empleados.models import Cargo, Ubigeo, Empleado


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class UbigeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubigeo
        fields = "__all__"


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"
