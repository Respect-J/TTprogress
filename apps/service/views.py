from rest_framework import generics
from .models import SingleService, Service
from .serializers import ServiceSerializer, SingleServiceSerializer
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
