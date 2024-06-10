from django.urls import path

from .views import UzbDataView, RusDataView

urlpatterns = [
    path("rus/", RusDataView.as_view(), name="data-get"),
    path("uzb/", UzbDataView.as_view(), name="data-get")


]
