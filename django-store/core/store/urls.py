from django.conf.urls import url
from django.urls import path,include
from .views import ProductsOfCategory,ProductsOfBrand,ProductsOfShop,ProductDetails,product_list

urlpatterns = [
                  path('categories/<slug:slug>/', ProductsOfCategory.as_view(), name='categories_product'),
                  path('brands/<slug:slug>/', ProductsOfBrand.as_view(), name='brands_product'),
                  path('products_of/<slug:slug>/', ProductsOfShop.as_view(), name='shops_product'),
                  path('products/<slug:slug>/', ProductDetails.as_view(), name='product_details'),
                  url(r'^list$', product_list)
              ]