from rest_framework import serializers
from apps.vet.models.diagnoses_model import Diagnoses


class DiagnosesSerializer(serializers.ModelSerializer):
    Diagnoses = serializers.StringRelatedField()

    class Meta:
        model = Diagnoses
        fields = "__all__"
