from django.conf.urls import url
from django.urls import path,include
from .views import ProductsOfCategory,ProductsOfBrand,ProductsOfShop,ProductDetails,product_list,comment_create,SearchField,add_score,ShopProductCreate

urlpatterns = [
                  path('categories/<slug:slug>/', ProductsOfCategory.as_view(), name='categories_product'),
                  path('brands/<slug:slug>/', ProductsOfBrand.as_view(), name='brands_product'),
                  path('products_of/<slug:slug>/', ProductsOfShop.as_view(), name='shops_product'),
                  path('products/<slug:slug>/', ProductDetails.as_view(), name='product_details'),
                  url(r'^list$', product_list),
                  path('comment/', comment_create, name='comment_create'),
                  path('search/', SearchField.as_view(), name='search'),
                  path('add_score/', add_score, name='add_score'),
                  path('create_shop_product/', ShopProductCreate.as_view(), name='create_shop_product'),


              ]