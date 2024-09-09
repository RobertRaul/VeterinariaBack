import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vet.models.recetas_model import Recetas
from apps.vet.serializers.receta_serializers import RecetaSerializer

class RecetaView(APIView):

    def get(self,request,pk):
        try:
            receta_data= Recetas.objects.filter(patient_id=pk)
            if receta_data:
                print(receta_data)
                return Response(RecetaSerializer(receta_data,many=True).data,status=status.HTTP_200_OK)
            return Response({'mensaje':"No existe ninguna receta asociado a esta mascota"},status=status.HTTP_404_NOT_FOUND)
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)