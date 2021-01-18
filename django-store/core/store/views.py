from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Product,ShopProduct
# Create your views here.


class ProductsOfCategory(ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        print(products)
        return HttpResponse(products)


class ProductsOfBrand(ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(brand__slug=self.kwargs['slug'])
        print(products)
        return HttpResponse(products)


class ProductsOfShop(ListView):
    model = ShopProduct

    def get(self, request, *args, **kwargs):
        shop_products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug'])
        print(shop_products)
        return HttpResponse(shop_products)





