from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse

from .forms import SignInForm, RegisterForm,AccountUpdate
from django.views.generic.edit import ModelFormMixin, UpdateView
from django.views.generic import CreateView, ListView
from django.views.generic.detail import BaseDetailView, DetailView
from .models import User, Shop,Address
from store.models import Like


class Login(LoginView):
    form_class = SignInForm
    template_name = 'homepage/login_form.html'


class Logout(LogoutView):
    pass


class Register(CreateView, ModelFormMixin):
    template_name = 'homepage/register_form.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        return render(request, 'homepage/register_form.html', context={'form': form})


class UserDetail(DetailView):
    model = User
    template_name = 'homepage/account_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data()
        context['account_addresses']=Address.objects.filter(user=context['object'])
        context['account_shops']=Shop.objects.filter(user=context['object'])
        context['favorites'] = Like.objects.filter(user=context['object'])
        # print(context['favorites'])
        return context

    # def get(self, request, *args, **kwargs):
    #     user_detail = User.objects.get(slug=self.kwargs['slug'])
    #     print(user_detail)
    #     return render(request,'homepage/account_profile.html',context={'user_detail':user_detail})


class ShopDetail(BaseDetailView):
    model = Shop

    def get(self, request, *args, **kwargs):
        shop_detail = Shop.objects.get(slug=self.kwargs['slug'])
        # print(shop_detail)
        return HttpResponse(shop_detail)


class AccountProfileUpdate(UpdateView):
    model = User
    form_class = AccountUpdate
    # fields = ['first_name','last_name','mobile_number','melli_code','email']
    template_name = 'homepage/update_user.html'

    def get_success_url(self):
        return reverse("user_details", kwargs={'slug': self.get_object().slug})

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(AccountProfileUpdate, self).get_context_data(**kwargs)
    #     # print('purya')
    #     print(context)
    #     return context


class AccountProfileUpdate(UpdateView):
    model = User
    form_class = AccountUpdate
    # fields = ['first_name','last_name','mobile_number','melli_code','email']
    template_name = 'homepage/update_user.html'

    def get_success_url(self):
        return reverse("user_details", kwargs={'slug': self.get_object().slug})

