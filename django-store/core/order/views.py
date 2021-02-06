import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import BasketForm
from django.views.generic import CreateView
from .models import Basket,BasketItem

# Create your views here.


# class CreateBasket(CreateView):
#
#     form_class = BasketForm
#
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             Basket.objects.create(user= request.user)
#             return render(request, 'base/header.html', context={})
#
#     def get_template_names(self):
#
#         return ['%s.html' % self.kwargs['template']]
# @csrf_exempt
# def create_basket(request):
#     user = request.user
#     basket = Basket.objects.create(user=user)
#     resopnse = {"basket":basket.user.email}
#
#     return HttpResponse(json.dumps(resopnse), status=201)

@csrf_exempt
def delete_basket(request):
    user = request.user
    basket = Basket.objects.get(user=user)
    basket.delete()
    resopnse = {"basket": user.email}
    return HttpResponse(json.dumps(resopnse), status=201)


# @csrf_exempt
# def add_to_basket(request):
#     data = json.loads(request.body)
#     shop_product = data['shop_product']
#     basket = data['basket_user']
#     basket_item = BasketItem.objects.create(basket_id=basket, shop_product_id=shop_product)

#


@csrf_exempt
def add_to_basket(request):
    user = request.user

    if user.is_authenticated:
        Basket.objects.get_or_create(user=user)
    else:
        pass

    data = json.loads(request.body)
    basket = user.user_baskets
    print(basket)
    shop_product = data['shop_product']
    basket_item = BasketItem.objects.create(basket_id=basket.id, shop_product_id=shop_product)
    resopnse = {"basket_item":basket_item.shop_product.product.title}
    return HttpResponse(resopnse, status=201)


@csrf_exempt
def create_basket(request):
    user = request.user
    basket=user.user_baskets
    items =  serializers.serialize('json', BasketItem.objects.filter(basket_id=basket))
    return HttpResponse(items, status=201)

