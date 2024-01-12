from django.db import models


class VendorApi(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)


class ShipperApi(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
