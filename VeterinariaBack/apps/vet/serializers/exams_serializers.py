from rest_framework import serializers
from apps.vet.models.exams_model import Exams


class ExamsSerializer(serializers.ModelSerializer):
    consults = serializers.StringRelatedField()

    class Meta:
        model = Exams
        fields = "__all__"
