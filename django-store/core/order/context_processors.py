from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from store.models import ShopProduct
from .models import Basket,BasketItem


def basket_items_proccessor(request):

            basket_items= BasketItem.objects.all
            return {'basket_items':basket_items}
