from django.db import models
from django.utils.translation import ugettext_lazy as _
from store.models import Brand


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
    subtitle = models.CharField(_('Sub title'), max_length=250)
    image = models.ImageField(_('Background image'), upload_to='siteview/best_brands/images')
    create_at = models.DateTimeField(_('Create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update at'), auto_now=True)
    action_text = models.CharField(_('Action text'), max_length=50)
    action_url = models.URLField(_('Action url'))

    def __str__(self):
        return self.title