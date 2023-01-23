from django.shortcuts import render

# Create your views here.
from .import_export import FoodSalesResource
from django.http import HttpResponse
from tablib import Dataset
from django.http import JsonResponse
from django.views import View
from .models import FoodSales


def import_data(request):
    if request.method == "POST":
        food_resource = FoodSalesResource()
        dataset = Dataset()
        new_foods = request.FILES['myfile']

        imported_data = dataset.load(new_foods.read())
        print('imported_data',imported_data)
        result = food_resource.import_data(
            dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            food_resource.import_data(
                dataset, dry_run=False)  # Actually import now

    return render(request, 'importer.html')



class SearchProductAPI(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)

        products = FoodSales.objects.filter(Product__icontains=query)
        product_list = [
            {
                'OrderDate': product.OrderDate,
                'Region': product.Region,
                'City': product.City,
                'Catagory': product.Catagory,
                'Product': product.Product,
                'Quantity': product.Quantity,
                'UnitPrice': product.UnitPrice,
            }
            for product in products
        ]

        return JsonResponse({'status': 'success', 'result': product_list})
    
    def post(self, request):
        product_name = request.POST.get('product_name')
        limit = int(request.POST.get('limit',5))
        products = FoodSales.objects.filter(
            Product__icontains=product_name)[:limit]
        product_list = [
            {
                'OrderDate': product.OrderDate,
                'Region': product.Region,
                'City': product.City,
                'Catagory': product.Catagory,
                'Product': product.Product,
                'Quantity': product.Quantity,
                'UnitPrice': product.UnitPrice,
            }
            for product in products
        ]
        return JsonResponse({'status': 'success', 'result': product_list})
