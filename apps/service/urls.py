from django.urls import path

from .views import ServiceListView, SingleServiceListView, ServiceSingleListView, PlanVipListView, PlanStandartListView

urlpatterns = [
    path("service/", ServiceListView.as_view(), name="service-get"),
    path("singlservice/", SingleServiceListView.as_view(), name="single-service-get"),
    path("getsingl/<int:pk>/", ServiceSingleListView.as_view(), name="service-single-get"),
    path("vip/<uuid:uuid>/", PlanVipListView.as_view(), name="planvip-get"),
    path("standart/<uuid:uuid>/", PlanStandartListView.as_view(), name="planstandart-get"),


]
