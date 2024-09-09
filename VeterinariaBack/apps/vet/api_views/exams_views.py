import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vet.models.exams_model import Exams
from apps.vet.serializers.exams_serializers import ExamsSerializer

class ExamsView(APIView):

    def get(self,request,pk):
        try:
            exams_data = Exams.objects.filter(consults=pk)
            if exams_data:
                return Response(ExamsSerializer(exams_data,many=True).data,status=status.HTTP_200_OK)
            return Response({"mensaje": "No existen examenes de esa cita"}, status=status.HTTP_404_NOT_FOUND)       
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)       