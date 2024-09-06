from rest_framework import serializers
from apps.vet.models.patient_model import Patient

class PatientsSerializer(serializers.ModelSerializer):
    breed = serializers.StringRelatedField()    

    class Meta:
        model = Patient
        fields = "__all__"
