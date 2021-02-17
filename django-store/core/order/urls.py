from django.urls import path
from .views import create_basket,add_to_basket,delete_basket,plus_basket_item,minus_basket_item,delete_basket_item,basket_page


urlpatterns = [
    path('create_basket/', create_basket, name='create_basket'),
    path('delete_basket/', delete_basket, name='delete_basket'),
    path('add_to_basket/', add_to_basket, name='add_to_basket'),
    path('plus_basket_item/', plus_basket_item, name='plus_basket_item'),
    path('minus_basket_item/', minus_basket_item, name='minus_basket_item'),
    path('delete_basket_item/', delete_basket_item, name='delete_basket_item'),
    path('user_basket/', basket_page, name='user_basket'),
    # path('mobiles/', MobileSlider.as_view(), name='mobiles'),

]
