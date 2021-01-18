from django.urls import path
from .views import Login, Register, Logout, UserDetail, ShopDetail

urlpatterns = [
                  path('login/', Login.as_view(), name='login'),
                  path('logout/', Logout.as_view(), name='logout'),
                  path('register/', Register.as_view(), name='register'),
                  path('user/<slug:slug>/', UserDetail.as_view(), name='user_details'),
                  path('shop/<slug:slug>/', ShopDetail.as_view(), name='shop_details')
              ]