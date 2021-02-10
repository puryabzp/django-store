import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView,DetailView
from .filters import MostExpensivePrice

from .models import Product,ShopProduct,ProductsImage,ProductMeta,Comment,Like
# Create your views here.


class ProductsOfCategory(ListView):
    model = Product
    template_name = 'homepage/category_products.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(category__slug=self.kwargs['slug'])
        print(products)
        return render(request, 'homepage/category_products.html', context={'products': products})


class ProductsOfBrand(ListView):
    model = Product
    template_name = 'homepage/category_products.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(brand__slug=self.kwargs['slug'])
        print(products)
        return render(request, 'homepage/category_products.html', context={'products': products})


class ProductsOfShop(ListView):
    model = ShopProduct
    template_name = 'homepage/shops_products.html'

    def get(self, request, *args, **kwargs):
        products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug'])
        print(products)
        return render(request, 'homepage/shops_products.html', context={'products': products})


class ProductDetails(DetailView):
    model = Product
    template_name = 'homepage/single_product.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data()
        context['shop_products'] = ShopProduct.objects.filter(product=context['object'])
        context['product_images'] = ProductsImage.objects.filter(product=context['object'])
        context['product_meta'] = ProductMeta.objects.filter(product=context['object'])
        context['product_comments'] = Comment.objects.filter(product=context['object'])
        # print(context)
        return context


def product_list(request):
    f = MostExpensivePrice(request.GET, queryset=Product.objects.all())
    return render(request, 'homepage/products.html', {'filter': f})



@csrf_exempt
def comment_create(request):
    data = json.loads(request.body)
    content = data['content']
    product = Product.objects.get(id=data['product_id'])
    user = request.user
    comment = Comment.objects.create(author=user, product=product, content=content)
    comment.save()
    comment_count = product.comments.count()
    print(comment_count)
    resopnse = {'author': str(user.email), 'content': comment.content,'comment_count': comment_count, 'comment_id': comment.id}

    return HttpResponse(json.dumps(resopnse), status=201)


class SearchField(ListView):
    template_name = 'base/header.html'
    paginate_by = 1
    model = Product

    def post(self, request, *args, **kwargs):
        search = request.POST['search']
        print(search)
        if not search:
            return render(request, 'homepage/empty_search.html', {})
        search_products = ShopProduct.objects.filter(Q(product__title__icontains=search) | Q(product__category__category_name__icontains=search))
        result = tuple(search_products)
        if not search_products:
            return render(request, 'homepage/not_found.html', {})
        return render(request, 'homepage/products.html', context={'search_products': result})


@csrf_exempt
def add_score(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    product = Product.objects.get(id=product_id)
    try:
        Like.objects.create(product=product,user=request.user)

    except:

        pass
    resopnse = {'like_count': product.like_count,}
    return HttpResponse(json.dumps(resopnse), status=201)

