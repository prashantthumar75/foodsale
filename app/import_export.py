from import_export import resources
from .models import FoodSales


class FoodSalesResource(resources.ModelResource):
    class Meta:
        model = FoodSales
