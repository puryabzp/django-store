from django.urls import path,include
from .views import ProductsOfCategory,ProductsOfBrand,ProductsOfShop

urlpatterns = [
                  path('categories/<slug:slug>/', ProductsOfCategory.as_view(), name='categories_product'),
                  path('brands/<slug:slug>/', ProductsOfBrand.as_view(), name='brands_product'),
                  path('products_of/<slug:slug>/', ProductsOfShop.as_view(), name='shops_product'),
              ]