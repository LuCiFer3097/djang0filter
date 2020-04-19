from django.db import models

# Create your models here.


class VendorType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Listings(models.Model):
    vendorname = models.CharField(max_length=20, null=False, blank=False)
    vegprice = models.DecimalField(
        max_digits=7, decimal_places=3, null=False, blank=False)
    nonvegprice = models.DecimalField(
        max_digits=7, decimal_places=3, null=False, blank=False)
    maxcap = models.IntegerField(null=True, blank=True)
    mincap = models.IntegerField(null=True, blank=True)
    town = models.ManyToManyField(City)
    venue = models.ManyToManyField(VendorType)
    address = models.CharField(max_length=20, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    highlights = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.vendorname
