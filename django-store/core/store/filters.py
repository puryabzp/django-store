from django_filters import FilterSet
from .models import ShopProduct


class MostExpensivePrice(FilterSet):
    class Meta:
        model = ShopProduct
        fields = {
            'price': ['gt'],
        }