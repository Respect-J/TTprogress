from django.urls import path

from .views import ServiceListView, SingleServiceListView, ServiceSingleListView

urlpatterns = [
    path("service/", ServiceListView.as_view(), name="service-get"),
    path("singlservice/", SingleServiceListView.as_view(), name="single-service-get"),
    path("getsingl/<int:pk>/", ServiceSingleListView.as_view(), name="service-single-list"),


]
