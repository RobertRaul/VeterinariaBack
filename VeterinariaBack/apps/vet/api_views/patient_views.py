import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.vet.models.patient_model import Patient
from apps.vet.serializers.patient_serializers import PatientsSerializer

class PatientViewDetail(APIView):

    def get(self, request,pk):
        try:
            #paciente_data = Patient.objects.prefetch_related('breed_id__specie_id').filter(client_id=pk)            
            paciente_data = Patient.objects.filter(client_id=pk).select_related('breed__specie')
            if paciente_data:
                return Response(PatientsSerializer(paciente_data,many=True).data,status=status.HTTP_200_OK)
            return Response({"mensaje": "No existe un email con estos datos"}, status=status.HTTP_404_NOT_FOUND)       
        except:
            tb = traceback.format_exc()
            print(tb)
            return Response({"SERVER ERROR"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)       