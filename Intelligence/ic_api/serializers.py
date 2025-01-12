from rest_framework import serializers
from .models import ReceivedData

class ReceivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedData
        fields = ['id', 'data', 'timestamp']
        read_only_fields = ['timestamp']