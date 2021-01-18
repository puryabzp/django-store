from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView

from .models import Product,ShopProduct,ProductsImage,ProductMeta,Comment
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


class ProductDetails(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data()
        context['shop_products'] = ShopProduct.objects.filter(product=context['object'])
        context['product_images'] = ProductsImage.objects.filter(product=context['object'])
        context['product_meta'] = ProductMeta.objects.filter(product=context['object'])
        context['product_comments'] = Comment.objects.filter(product=context['object'])
        return context


