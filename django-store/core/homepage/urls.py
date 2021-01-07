from django.urls import path
from .views import slide_view

urlpatterns = [
    path('home/', slide_view, name='home'),

]
