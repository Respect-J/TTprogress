from rest_framework import generics
from .models import RusData, UzbData
from .serializers import RusDataSerializer, UzbDataSerializer


class RusDataView(generics.ListAPIView):
    queryset = RusData.objects.all()
    serializer_class = RusDataSerializer


class UzbDataView(generics.ListAPIView):
    queryset = UzbData.objects.all()
    serializer_class = UzbDataSerializer
