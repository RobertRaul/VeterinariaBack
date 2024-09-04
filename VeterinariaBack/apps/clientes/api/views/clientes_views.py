from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.clientes.models import Clientes
from apps.clientes.api.serializers import ClienteSerializer


# VIEWSET
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(pk=pk).first()

    def list(self, request):
        cliente_serializer = self.get_serializer(self.get_queryset(), many=True)
        # data = {
        #     "total": self.get_queryset().count(),
        #     "totalNotFiltered": self.get_queryset().count(),
        #     "rows": cargo_serializer.data
        # }
        return Response(cliente_serializer.data, status=status.HTTP_200_OK)

    # METODO CREAR
    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cliente Creado correctamente!"},
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
            cliente_serializer = ClienteSerializer(cargo)
            return Response(cliente_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un Cliente con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # METODO UPDATE
    def update(self, request, pk=None):
        if self.get_queryset(pk=pk):
            # send information to serializer referencing the instance
            cliente_serializer = self.serializer_class(
                self.get_queryset(pk=pk), data=request.data
            )
            if cliente_serializer.is_valid():
                cliente_serializer.save()
                return Response(
                    {"message": "Cliente actualizado correctamente!"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "", "Error": cliente_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # METODO ELIMINAR
    def destroy(self, request, pk=None):
        cliente = self.get_queryset().filter(pk=pk).first()  # get instance
        if cliente:
            cliente.Estado = False
            return Response(
                {"message": "Cliente eliminado correctamente!"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "No existe un Cliente con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class Login(APIView):
    model = Clientes
    serializer_class = ClienteSerializer

       # METODO LOGIN
    def post(self, request,):
        email = request.data.get("email")
        password = request.data.get("password")
        cliente = self.serializer_class().Meta.model.objects.filter(email=email,password=password,Estado=True).first()        
        if cliente:            
            cliente_serializer = ClienteSerializer(cliente)
            return Response(cliente_serializer.data, status=status.HTTP_200_OK)            
        return Response({"mensaje": "No existe un email con estos datos"}, status=status.HTTP_404_NOT_FOUND)       