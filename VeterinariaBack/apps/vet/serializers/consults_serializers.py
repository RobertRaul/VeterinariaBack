from rest_framework import serializers
from apps.vet.models.consults_model import Consults


class ConsultsSerializer(serializers.ModelSerializer):
    consults = serializers.StringRelatedField()

    class Meta:
        model = Consults
        fields = "__all__"
