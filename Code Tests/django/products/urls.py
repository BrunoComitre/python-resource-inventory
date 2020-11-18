from django.urls import path
from .views import list_products, create_product, update_product, delete_product


app_name = 'products'
urlpatterns = [
    # ex: /products/
    path('', list_products, name='list_product'),  # READ
    # ex: /products/5/
    path('new/', create_product, name='create_product'),  # GET
    # ex: /products/5/
    path('update/<int:id>/', update_product, name='update_product'),  # PUT
    # ex: /products/5/
    path('delete/<int:id>/', delete_product, name='delete_product'),  # DELETE
]

# CRUD -  CREATE, READ, UPDATE, DELETE
#          POST , GET ,   PUT , DELETE
