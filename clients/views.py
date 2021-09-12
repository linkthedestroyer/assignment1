from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Count

from .models import Client, Comment, models


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/client_list.html"

    def get_queryset(self):
        new_context = Client.objects.annotate(vehicle_count=Count("vehicles")).filter(
            author=self.request.user,
        )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        return context


class ClientDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/client_detail.html"
    login_url = "login"

    def test_func(self):
        return self.request.user.id == Client.objects.get(pk=self.kwargs["pk"]).author.id


class ClientUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Client
    fields = ("name", "notes", "address", "city", "state", "zipcode", "email", "cell_phone", "acct_number")
    template_name = "clients/client_edit.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.id == Client.objects.get(pk=self.kwargs["pk"]).author.id


class ClientDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "clients/client_delete.html"
    success_url = reverse_lazy("client_list")

    def test_func(self):
        return self.request.user.id == Client.objects.get(pk=self.kwargs["pk"]).author.id


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/client_new.html"
    fields = ("name", "notes", "address", "city", "state", "zipcode", "email", "cell_phone", "acct_number")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "clients/comment_new.html"
    fields = ("comment",)
    login_url = "login"

    def form_valid(self, form):
        form.instance.client = Client.objects.get(pk=self.kwargs["pk"])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.id == Client.objects.get(pk=self.kwargs["pk"]).author.id
