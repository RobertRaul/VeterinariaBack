from rest_framework import serializers
from apps.vet.models.recetas_model import Recetas


class RecetaSerializer(serializers.ModelSerializer):
#    specie = serializers.StringRelatedField()

    class Meta:
        model = Recetas
        fields = "__all__"
