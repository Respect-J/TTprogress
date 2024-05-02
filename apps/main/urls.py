from django.urls import path

from .views import ContactListView, UniverLogoListView, MentorsListView, CertificatesListView

urlpatterns = [
    path("contacts/", ContactListView.as_view(), name="Contact-get"),
    path("univerlogos/", UniverLogoListView.as_view(), name="Logo-get"),
    path("mentors/", MentorsListView.as_view(), name="Mentor-get"),
    path("certificates/", CertificatesListView.as_view(), name="Certificates-get"),

]
