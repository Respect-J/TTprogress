from rest_framework import serializers
from .models import Service, SingleService, PlanVip, PlanStandart


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class SingleServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleService
        fields = "__all__"


class PlanVipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanVip
        fields = "__all__"


class PlanStandartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanStandart
        fields = "__all__"
