from store.models import Category,Brand,Product,ShopProduct
from account.models import Shop


def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}


def brands_processor(request):
    brands = Brand.objects.all()
    return {'brands': brands}


def shops_processor(request):
    shops = Shop.objects.all()
    return {'shops': shops}


def mobile_processor(request):
    mobiles = ShopProduct.objects.filter(product__category__category_name='mobile')
    return {'mobiles': mobiles}