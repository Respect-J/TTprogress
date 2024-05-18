from rest_framework import generics
from .models import Contacts, Mentors, Certificates, UniverLogo, AboutMentors, About, Stats, WhyUs, Hero
from .serializers import ContactsSerializer, MentorsSerializer, CertificatesSerializer, UniverLogoSerializer, \
    HeroSerializer, WhyUsSerializer, AboutSerializer, StatsSerializer, AboutMentorsSerializer


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


class StatsListView(generics.ListAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer


class HeroListView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutMentorsListView(generics.ListAPIView):
    queryset = AboutMentors.objects.all()
    serializer_class = AboutMentorsSerializer


class WhyUsListView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = WhyUsSerializer
