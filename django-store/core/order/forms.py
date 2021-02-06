from django import forms
from django.utils.translation import ugettext_lazy as _


class BasketForm(forms.Form):

    user = forms.CharField(label=_(''),widget=forms.TextInput)


class BasketItemForm(forms.Form):
    shop_product = forms.CharField(label=_(''), widget=forms.TextInput)
    basket = forms.CharField(label=_(''), widget=forms.TextInput)
    count = forms.CharField(label=_(''), widget=forms.TextInput)
    price = forms.CharField(label=_(''), widget=forms.TextInput)