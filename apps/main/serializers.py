from rest_framework import serializers

from .models import Contacts, Certificates, Mentors, UniverLogo, AboutMentors, About, Stats, WhyUs, Hero


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = "__all__"


class MentorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = "__all__"


class UniverLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniverLogo
        fields = "__all__"


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class AboutMentorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMentors
        fields = "__all__"


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = "__all__"
