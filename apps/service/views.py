from rest_framework import generics
from .models import SingleService, Service, PlanVip, PlanStandart
from .serializers import ServiceSerializer, SingleServiceSerializer, PlanVipSerializer, PlanStandartSerializer
from django.shortcuts import get_object_or_404

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class SingleServiceListView(generics.ListAPIView):
    queryset = SingleService.objects.all()
    serializer_class = SingleServiceSerializer


class ServiceSingleListView(generics.ListAPIView):
    serializer_class = SingleServiceSerializer

    def get_queryset(self):
        service_id = self.kwargs["pk"]
        service = get_object_or_404(Service, id=service_id)
        return SingleService.objects.filter(service=service)


class PlanVipListView(generics.ListAPIView):
    serializer_class = PlanVipSerializer

    def get_queryset(self):
        service_id = self.kwargs["uuid"]
        service = get_object_or_404(SingleService, id=service_id)
        return PlanVip.objects.filter(single=service)


class PlanStandartListView(generics.ListAPIView):
    serializer_class = PlanStandartSerializer

    def get_queryset(self):
        service_id = self.kwargs["uuid"]
        service = get_object_or_404(SingleService, id=service_id)
        return PlanStandart.objects.filter(single=service)
