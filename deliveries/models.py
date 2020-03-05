from django.db import models
from django.contrib.auth.models import User

class QuantityMesurements(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    measurements = models.ForeignKey(QuantityMesurements, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Delivery(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    dateTime = models.DateTimeField(auto_now=False)
    # time = models.TimeField(auto_now=False)
    class Meta:
        ordering = ('dateTime', )

    # def extract_date(delivery):
    #     'extracts the starting date from a delivery'
    #     return delivery.dateTime.date()
    # def __str__(self):
    #     return "{} {} {} delivery to {}".format(item.quantity, item.name, item.measurements.name, customer.username)

