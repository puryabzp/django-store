from django.urls import path
from .views import HomeView,home_view

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', home_view, name='home_view'),
    # path('mobiles/', MobileSlider.as_view(), name='mobiles'),

]
