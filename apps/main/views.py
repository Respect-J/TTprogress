from rest_framework import generics
from .models import Contacts, Mentors, Certificates, UniverLogo
from .serializers import ContactsSerializer, MentorsSerializer, CertificatesSerializer, UniverLogoSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class MentorsListView(generics.ListAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorsSerializer


class CertificatesListView(generics.ListAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer


class UniverLogoListView(generics.ListAPIView):
    queryset = UniverLogo.objects.all()
    serializer_class = UniverLogoSerializer