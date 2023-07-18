from .models import Booth
from rest_framework import serializers

class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')
