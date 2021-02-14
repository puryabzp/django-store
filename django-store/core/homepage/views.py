from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import SlideShow, BestBrand, ExceptionalDiscounts
from store.models import Product


# Create your views here.


def slide_view(request):
    return render(request, 'homepage/home_page.html', context={})


class HomeView(TemplateView):
    template_name = 'homepage/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['slide_list'] = SlideShow.objects.all()
        context['best_brands'] = BestBrand.objects.all()
        context['discounts'] = ExceptionalDiscounts.objects.all()
        return context


# class MobileSlider(TemplateView):
#     model = Product
#     template_name = 'homepage/home_page.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(MobileSlider, self).get_context_data()
#         context['mobiles'] = Product.objects.filter(category__category_name='mobile')
#         print(context['mobiles'])
#         return context
def home_view(request):
    return redirect('home')
