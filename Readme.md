Product Search API

This API allows you to search for products by product name and limits the response to 5 items.
URL endpoint : GET and POST '/search_product/'

Install the dependencies
pip install -r requirements.txt

Run the server
python manage.py runserver

Usage
Make a POST request to the endpoint '/search_product/' with product_name in the request body.
The API will return a maximum of 5 products that match the product_name provided in the request.

