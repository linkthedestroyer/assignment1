from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from clients.models import Client


class Vehicle(models.Model):
    make = models.CharField(max_length=50, blank=False, null=False, default=" ")
    model = models.CharField(max_length=50, blank=True, null=True, default=" ")
    VIN_number = models.CharField(max_length=50, default=" ")
    date_of_purchase = models.DateTimeField(default=datetime.now())
    date_of_last_service = models.DateTimeField(default=datetime.now())
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="vehicles",)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse("vehicle_detail", args=[str(self.id)])
