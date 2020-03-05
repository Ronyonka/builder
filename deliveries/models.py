from django.db import models
from django.contrib.auth.models import User

class QuantityMesurements(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Items(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    measurements = models.ForeignKey(QuantityMesurements, on_delete=models.CASCADE, null=False)

class Delivery(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)


