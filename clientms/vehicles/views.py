from clients.models import Client
from django.contrib.auth.mixins import LoginRequiredMixin  # New
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Vehicle


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = "vehicles/vehicle_list.html"

    def get_queryset(self):
        return Vehicle.objects.filter(client__exact=self.kwargs["clientId"])

    def get_context_data(self, **kwargs):
        context = super(VehicleListView, self).get_context_data(**kwargs)
        return context


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = "vehicles/vehicle_detail.html"
    login_url = "login"


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ("make", "model", "VIN_number", "date_of_purchase", "date_of_last_service", "client")
    template_name = "vehicles/vehicle_edit.html"


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = "vehicles/vehicle_delete.html"
    success_url = reverse_lazy("vehicle_list")


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = "vehicles/vehicle_new.html"
    fields = ("make", "model", "VIN_number", "date_of_purchase", "date_of_last_service")
    login_url = "login"

    def form_valid(self, form):
        form.instance.client = Client.objects.get(pk=self.kwargs["clientId"])
        form.instance.author = self.request.user
        return super().form_valid(form)
