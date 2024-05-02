from rest_framework import serializers

from .models import Service, SingleService


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class SingleServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleService
        fields = "__all__"


