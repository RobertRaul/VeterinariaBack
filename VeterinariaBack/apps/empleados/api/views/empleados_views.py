from rest_framework.views import APIView
from rest_framework import viewsets, status
from apps.empleados.models import Cargo
from apps.empleados.api.serializers import (
    CargoSerializer,
)
from rest_framework.response import Response


class CargoApiView(APIView):

    def get(self, request):
        cargos = Cargo.objects.all()
        cargos_serializer = CargoSerializer(cargos, many=True)
        return Response(cargos_serializer.data)


# VIEWSET
class CargoViewSet(viewsets.ModelViewSet):
    serializer_class = CargoSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(pk=pk).first()

    def list(self, request):
        cargo_serializer = self.get_serializer(self.get_queryset(), many=True)
        # data = {
        #     "total": self.get_queryset().count(),
        #     "totalNotFiltered": self.get_queryset().count(),
        #     "rows": cargo_serializer.data
        # }
        return Response(cargo_serializer.data, status=status.HTTP_200_OK)

    # METODO CREAR
    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cargo creado correctamente!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "", "Error ": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # METODO BUSCAR
    def retrieve(self, request, pk=None):
        cargo = self.get_queryset(pk=pk)
        if cargo:
            cargo_serializer = CargoSerializer(cargo)
            return Response(cargo_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un Cargo con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # METODO UPDATE
    def update(self, request, pk=None):
        if self.get_queryset(pk=pk):
            # send information to serializer referencing the instance
            cargo_serializer = self.serializer_class(
                self.get_queryset(pk=pk), data=request.data
            )
            if cargo_serializer.is_valid():
                cargo_serializer.save()
                return Response(
                    {"message": "Cargo actualizado correctamente!"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "", "Error": cargo_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # METODO ELIMINAR
    def destroy(self, request, pk=None):
        cargo = self.get_queryset().filter(pk=pk).first()  # get instance
        if cargo:
            #cargo.state = False
            self.perform_destroy(cargo)
            return Response(
                {"message": "Cargo eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No existe un Cargo con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )
