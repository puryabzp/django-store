from django.db import models
from django.utils.translation import ugettext_lazy as _
from store.models import Brand,ShopProduct
from account.models import Shop


# Create your models here.

class SlideShow(models.Model):
    title = models.CharField(_('Title'), max_length=250)
    subtitle = models.CharField(_('Sub title'), max_length=250)
    image = models.ImageField(_('Background image'), upload_to='siteview/slide_show/images')
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update at'), auto_now=True)
    action_text = models.CharField(_('Action text'), max_length=50)
    action_url = models.URLField(_('Action url'))

    def __str__(self):
        return self.title


class BestBrand(models.Model):
    brand = models.ForeignKey(Brand, verbose_name=_('brand'), related_name='best_brand', related_query_name='best_brand',
                              on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=250)
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update at'), auto_now=True)

    def __str__(self):
        return self.brand.brand_name


class ExceptionalDiscounts(models.Model):
    product = models.ForeignKey(ShopProduct, verbose_name=_('product'), related_name='discount_product', related_query_name='discount_product', on_delete=models.CASCADE)
    discount = models.DecimalField(_('discount'),default=0.00, decimal_places=0, max_digits=100)
    slug = models.SlugField(_('slug'), unique=True, null=True, blank=True)
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update at'), auto_now=True)

    def __str__(self):
        return self.product.product.title

    @property
    def final_pay(self):

        final_pay = self.product.price - (self.product.price * (self.discount / 100))
        return int(final_pay)