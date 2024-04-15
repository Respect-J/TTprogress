from rest_framework import generics
from .models import Contacts
from .serializers import ContactsSerializer


class ContactListView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
