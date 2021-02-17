from store.models import Category, Brand, Product, ShopProduct
from account.models import Shop


def categories_processor(request):
    categories = Category.objects.filter(parent__isnull=True)
    childs = Category.objects.filter(parent__isnull=False)

    return {'categories': categories, 'childs': childs}


# def child_proccessor(request):
#
#     child_category= Category.objects.all()
#     return {'childs' :child_category}


def brands_processor(request):
    brands = Brand.objects.all()
    return {'brands': brands}


def shops_processor(request):
    shops = Shop.objects.all()
    return {'shops': shops}


def mobile_processor(request):
    mobiles = ShopProduct.objects.filter(product__category__category_name='موبایل')
    return {'mobiles': mobiles}
