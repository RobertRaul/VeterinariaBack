from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.vet.models.client_model import Client
from apps.vet.serializers.client_serializers import ClientSerializer


class LoginView(APIView):    

       # METODO LOGIN
    def post(self, request,):
        email = request.data.get("email")
        password = request.data.get("password")
        cliente = Client.objects.filter(email=email,password=password,status=1).first()                        
        if cliente:                        
            return Response( ClientSerializer(cliente).data, status=status.HTTP_200_OK)            
        return Response({"mensaje": "No existe un email con estos datos"}, status=status.HTTP_404_NOT_FOUND)       