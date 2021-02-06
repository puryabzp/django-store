from django.urls import path
from .views import create_basket,add_to_basket,delete_basket


urlpatterns = [
    path('create_basket/', create_basket, name='create_basket'),
    path('delete_basket/', delete_basket, name='delete_basket'),
    path('add_to_basket/', add_to_basket, name='add_to_basket'),
    # path('mobiles/', MobileSlider.as_view(), name='mobiles'),

]
