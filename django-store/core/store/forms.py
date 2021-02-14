from django import forms
from .models import ShopProduct, Product
from account.models import Shop


class AddShopProduct(forms.ModelForm):
    class Meta:
        model = ShopProduct
        fields = ['shop', 'number_in_stock', 'product', 'price']
