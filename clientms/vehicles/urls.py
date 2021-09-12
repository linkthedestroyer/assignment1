from django.urls import path

from .views import VehicleListView, VehicleUpdateView, VehicleDetailView, VehicleDeleteView, VehicleCreateView

urlpatterns = [
    path("<int:pk>/edit/", VehicleUpdateView.as_view(), name="vehicle_edit"),
    path("<int:pk>/", VehicleDetailView.as_view(), name="vehicle_detail"),
    path("<int:pk>/delete/", VehicleDeleteView.as_view(), name="vehicle_delete"),
    path("new/client/<int:clientId>/", VehicleCreateView.as_view(), name="vehicle_new"),
    path("client/<int:clientId>/", VehicleListView.as_view(), name="vehicle_list"),
]
