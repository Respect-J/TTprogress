from rest_framework import serializers
from .models import RusData, UzbData


class RusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RusData
        fields = '__all__'


class UzbDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzbData
        fields = '__all__'
