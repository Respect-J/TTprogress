from rest_framework import serializers

from .models import Contacts, Certificates, Mentors, UniverLogo


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
        model = Certificates
        fields = "__all__"
