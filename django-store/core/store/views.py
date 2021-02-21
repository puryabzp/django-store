import json
from django.db.models import Q, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView
from .filters import MostExpensivePrice
from .forms import AddShopProduct

from .models import Product, ShopProduct, ProductsImage, ProductMeta, Comment, Like


class ProductsOfCategory(ListView):
    model = Product
    template_name = 'homepage/category_products.html'

    def get(self, request, *args, **kwargs):
        try:
            products = Product.objects.filter(category__slug=self.kwargs['slug'])
            return render(request, 'homepage/category_products.html', context={'products': products})
        except:
            return render(request, 'homepage/products.html', context={})

    def post(self, request, *args, **kwargs):

        if request.POST['filter'] == 'alphabet':
            products = Product.objects.filter(category__slug=kwargs['slug']).order_by('title')
            return render(request, 'homepage/category_products.html', context={'products': products})

        elif request.POST['filter'] == 'expensive':
            products = Product.objects.filter(category__slug=kwargs['slug']).order_by('-products__price')
            return render(request, 'homepage/category_products.html', context={'products': products})
        elif request.POST['filter'] == 'cheap':
            products = Product.objects.filter(category__slug=kwargs['slug']).order_by('products__price')
            return render(request, 'homepage/category_products.html', context={'products': products})
        elif request.POST['filter'] == 'available':
            products = Product.objects.filter(category__slug=kwargs['slug']).exclude(products__number_in_stock=0)
            if products:
                return render(request, 'homepage/category_products.html', context={'products': products})
            else:
                products = Product.objects.filter(category__slug=kwargs['slug'])
                return render(request, 'homepage/category_products.html', context={'products': products})
        elif request.POST['filter'] == 'old':
            products = Product.objects.filter(category__slug=kwargs['slug']).order_by('created_at')
            return render(request, 'homepage/category_products.html', context={'products': products})
        elif request.POST['filter'] == 'new':
            products = Product.objects.filter(category__slug=kwargs['slug']).order_by('-created_at')
            return render(request, 'homepage/category_products.html', context={'products': products})

        return redirect('home')

    # def get_ordering(self):
    #     ordering = self.request.GET['q']
    #     return self.get_queryset().order_by(self,ordering)


class ProductsOfBrand(ListView):
    model = Product
    template_name = 'homepage/products_of_brand.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        try:
            products = Product.objects.filter(brand__slug=self.kwargs['slug'])
            # print(products)
            return render(request, self.template_name, context={'products': products})

        except:
            return render(request, 'homepage/products.html', context={})

    def post(self, request, *args, **kwargs):
        if request.POST['filter'] == 'alphabet':
            products = Product.objects.filter(brand__slug=kwargs['slug']).order_by('title')
            return render(request, 'homepage/products_of_brand.html', context={'products': products})

        elif request.POST['filter'] == 'expensive':
            products = Product.objects.filter(brand__slug=kwargs['slug']).order_by('-products__price')
            return render(request, 'homepage/products_of_brand.html', context={'products': products})
        elif request.POST['filter'] == 'cheap':
            products = Product.objects.filter(brand__slug=kwargs['slug']).order_by('products__price')
            return render(request, 'homepage/products_of_brand.html', context={'products': products})
        elif request.POST['filter'] == 'available':
            products = Product.objects.filter(brand__slug=kwargs['slug']).exclude(products__number_in_stock=0)
            return render(request, 'homepage/products_of_brand.html', context={'products': products})
        elif request.POST['filter'] == 'old':
            products = Product.objects.filter(brand__slug=kwargs['slug']).order_by('created_at')
            return render(request, 'homepage/products_of_brand.html', context={'products': products})
        elif request.POST['filter'] == 'new':
            products = Product.objects.filter(brand__slug=kwargs['slug']).order_by('-created_at')
            return render(request, 'homepage/products_of_brand.html', context={'products': products})
        return redirect('home')


class ProductsOfShop(ListView):
    model = ShopProduct
    template_name = 'homepage/shops_products.html'

    def get(self, request, *args, **kwargs):
        try:
            products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug'])
            # print(products)
            return render(request, 'homepage/shops_products.html', context={'products': products})
        except:
            return render(request, 'homepage/products.html', context={})

    def post(self, request, *args, **kwargs):
        # if request.POST['janebi']:
        #     return redirect('login')
        try:
            if request.POST['filter'] == 'alphabet':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).order_by('product__title')
                return render(request, 'homepage/shops_products.html', context={'products': products})
            elif request.POST['filter'] == 'expensive':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).order_by('-price')
                return render(request, 'homepage/shops_products.html', context={'products': products})
            elif request.POST['filter'] == 'cheap':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).order_by('price')
                return render(request, 'homepage/shops_products.html', context={'products': products})
            elif request.POST['filter'] == 'available':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).exclude(number_in_stock=0)
                return render(request, 'homepage/shops_products.html', context={'products': products})
            elif request.POST['filter'] == 'old':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).order_by('created_at')
                return render(request, 'homepage/shops_products.html', context={'products': products})
            elif request.POST['filter'] == 'new':
                print(request.POST)
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug']).order_by('-created_at')
                return render(request, 'homepage/shops_products.html', context={'products': products})
        except:
            try:
                cat = request.POST.get('janebi')
                shop_name = request.POST.get('shop')
                print(cat, shop_name)
                print(request.POST)
                products = ShopProduct.objects.filter(shop__name=shop_name).filter(product__category__slug=cat)
                return render(request, 'homepage/shops_products.html', context={'products': products})
            except:
                products = ShopProduct.objects.filter(shop__slug=self.kwargs['slug'])
                print(type(products))
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


@csrf_exempt
def comment_create(request):
    data = json.loads(request.body)
    content = data['content']
    product = Product.objects.get(id=data['product_id'])
    user = request.user
    comment = Comment.objects.create(author=user, product=product, content=content)
    comment.save()
    comment_count = product.comments.count()
    # print(comment_count)
    response = {'author': str(user.email), 'content': comment.content, 'comment_count': comment_count,
                'comment_id': comment.id}

    return HttpResponse(json.dumps(response), status=201)


class SearchField(ListView):
    template_name = 'base/header.html'
    paginate_by = 1
    model = Product

    def post(self, request, *args, **kwargs):
        search = request.POST['search']
        # print(search)
        if not search:
            return render(request, 'homepage/empty_search.html', {})
        search_products = ShopProduct.objects.filter(
            Q(product__title__icontains=search) | Q(product__category__category_name__icontains=search))
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
        Like.objects.create(product=product, user=request.user)

    except:

        pass
    response = {'like_count': product.like_count, }
    return HttpResponse(json.dumps(response), status=201)


class ShopProductCreate(CreateView):
    model = ShopProduct
    form_class = AddShopProduct
    template_name = 'homepage/add_shop_product.html'
    success_url = 'home'

    def get_success_url(self):
        # print(self.object)
        return reverse('user_details', kwargs={'slug': self.object.shop.user.slug})
