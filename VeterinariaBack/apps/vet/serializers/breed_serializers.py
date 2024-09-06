from rest_framework import serializers
from apps.vet.models.breed_model import Breed


class BreedSerializer(serializers.ModelSerializer):
    specie = serializers.StringRelatedField()

    class Meta:
        model = Breed
        fields = "__all__"
