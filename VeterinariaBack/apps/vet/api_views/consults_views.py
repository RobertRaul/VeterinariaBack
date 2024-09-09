import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.vet.models.consults_model import Consults
from apps.vet.serializers.consults_serializers import ConsultsSerializer

class ConsultView(APIView):

    def get(self, request,pk):
        try:
            #paciente_data = Patient.objects.prefetch_related('breed_id__specie_id').filter(client_id=pk)            
            consult_data = Consults.objects.filter(patient=pk)
            if consult_data:
                return Response(ConsultsSerializer(consult_data,many=True).data,status=status.HTTP_200_OK)
            return Response({"mensaje": "No existen consultas"}, status=status.HTTP_404_NOT_FOUND)       
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)       
            