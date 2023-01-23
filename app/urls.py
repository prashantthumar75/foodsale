from django.urls import path, include
from . import views

urlpatterns = [
    path('import/', views.import_data, name='import_file'),
    path('search_product/', views.SearchProductAPI.as_view(), name='search_product'),
]
