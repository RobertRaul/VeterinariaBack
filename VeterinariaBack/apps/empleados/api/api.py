from rest_framework.views import APIView
from apps.empleados.models import Cargo
from apps.empleados.api.serializers import (
    CargoSerializer,
    UbigeoSerializer,
    EmpleadoSerializer,
)
from rest_framework.response import Response


class CargoApiView(APIView):

    def get(self, request):
        cargos = Cargo.objects.all()
        cargos_serializer = CargoSerializer(cargos, many=True)
        return Response(cargos_serializer.data)
