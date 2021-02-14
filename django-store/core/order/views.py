import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import BasketForm
from django.views.generic import CreateView
from .models import Basket, BasketItem


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
@csrf_exempt
def create_basket(request):
    user = request.user
    basket = Basket.objects.create(user=user)
    response = {"basket": basket.user.email}

    return HttpResponse(json.dumps(response), status=201)


@csrf_exempt
def delete_basket(request):
    user = request.user
    basket = Basket.objects.get(user=user)
    basket.delete()
    resopnse = {"basket": user.email}
    return HttpResponse(json.dumps(resopnse), status=201)


@csrf_exempt
def add_to_basket(request):
    user = request.user

    if user.is_authenticated:
        Basket.objects.get_or_create(user=user)
    else:
        pass

    data = json.loads(request.body)
    basket = user.user_baskets
    shop_product = data['shop_product']
    try:
        basket_item = BasketItem.objects.create(basket_id=basket.id, shop_product_id=shop_product)
        basket_item.count += 1
        basket_item.save()
        response = {"basket_item": basket_item.shop_product.product.title}
        return HttpResponse(response, status=201)
    except:
        pass
    return HttpResponse('response', status=201)


@csrf_exempt
def create_basket(request):
    user = request.user
    basket = user.user_baskets
    items = serializers.serialize('json', BasketItem.objects.filter(basket_id=basket))
    return HttpResponse(items, status=201)


@csrf_exempt
def plus_basket_item(request):
    data = json.loads(request.body)
    basket_item_id = data['basket_item_id']
    basket_item = BasketItem.objects.get(id=basket_item_id)
    basket_item.count += 1
    basket_item.save()
    price = basket_item.count * basket_item.shop_product.price
    response = {"basket_item_count": basket_item.count, 'basket_item_id': basket_item.id, 'price': str(price)}
    # print(response)
    return HttpResponse(json.dumps(response), status=201)


@csrf_exempt
def minus_basket_item(request):
    response = {}
    data = json.loads(request.body)
    basket_item_id = data['basket_item_id']
    basket_item = BasketItem.objects.get(id=basket_item_id)
    if basket_item.count > 0:
        try:
            basket_item.count -= 1
            basket_item.save()
            price = basket_item.count * basket_item.shop_product.price
            response = {"basket_item_count": basket_item.count, 'basket_item_id': basket_item.id, 'price': str(price)}
        except:
            pass
            # print(response)
    return HttpResponse(json.dumps(response), status=201)


@csrf_exempt
def delete_basket_item(request):
    response = {}
    data = json.loads(request.body)
    basket_item_id = data['basket_item_id']
    try:
        basket_item = BasketItem.objects.get(id=basket_item_id)
        basket_item.delete()
        response = {"basket_item": basket_item_id}
    except BasketItem.DoesNotExist:
        pass
    return HttpResponse(json.dumps(response), status=201)
