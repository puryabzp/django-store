from store.models import ShopProduct
from .models import Basket,BasketItem


def basket_items_proccessor(request):
    try:
        basket_items= BasketItem.objects.filter(basket__user=request.user)
        return {'basket_items':basket_items}
    except BasketItem.DoesNotExist:
        pass