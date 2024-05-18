from django.urls import path

from .views import ContactListView, UniverLogoListView, MentorsListView, CertificatesListView, HeroListView, \
    WhyUsListView, StatsListView, AboutListView, AboutMentorsListView

urlpatterns = [
    path("contacts/", ContactListView.as_view(), name="Contact-get"),
    path("univerlogos/", UniverLogoListView.as_view(), name="Logo-get"),
    path("mentors/", MentorsListView.as_view(), name="Mentor-get"),
    path("certificates/", CertificatesListView.as_view(), name="Certificates-get"),

    path("hero/", HeroListView.as_view(), name="hero-get"),
    path("whyus/", WhyUsListView.as_view(), name="whyus-get"),
    path("stats/", StatsListView.as_view(), name="stats-get"),
    path("aboutmentor/", AboutMentorsListView.as_view(), name="aboutmentors-get"),
    path("about/", AboutListView.as_view(), name="about-get"),

]
