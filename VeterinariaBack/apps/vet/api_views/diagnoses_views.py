import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vet.models.diagnoses_model import Diagnoses
from apps.vet.serializers.diagnoses_serializers import DiagnosesSerializer

class DiagnosesView(APIView):

    def get(self,request,pk):
        try:
            diagnoses_data= Diagnoses.objects.filter(consults=pk)
            if diagnoses_data:
                print(diagnoses_data)
                return Response(DiagnosesSerializer(diagnoses_data,many=True).data,status=status.HTTP_200_OK)
            return Response({'mensaje':"No existe ningun diagnostico asociado a esta consulta"},status=status.HTTP_404_NOT_FOUND)
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)