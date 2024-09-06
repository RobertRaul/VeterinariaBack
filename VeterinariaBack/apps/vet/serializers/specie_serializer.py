from rest_framework import serializers
from apps.vet.models.specie_model import Specie


class SpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specie
        fields = "__all__"
