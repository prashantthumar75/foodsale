from django.db import models

# Create your models here.

class FoodSales(models.Model):

    OrderDate = models.DateField(blank=True, null=True)
    Region = models.CharField(max_length=90, blank=False, null=True, default='')
    City = models.CharField(max_length=90, blank=False, null=True, default='')
    Catagory = models.CharField(max_length=90, blank=False, null=True, default='')
    Product = models.CharField(max_length=90, blank=False, null=True, default='')
    Quantity = models.IntegerField(blank=False, null=True, default=0)
    UnitPrice = models.FloatField(blank=False, null=True, default=0)
