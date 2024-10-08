from rest_framework import serializers
from apps.vet.models.client_model import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
