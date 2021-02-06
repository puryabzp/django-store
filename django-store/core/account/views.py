from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignInForm, RegisterForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView,ListView
from django.views.generic.detail import BaseDetailView
from .models import User,Shop


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


class UserDetail(BaseDetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user_detail = User.objects.get(slug=self.kwargs['slug'])
        print(user_detail)
        return HttpResponse(user_detail)


class ShopDetail(BaseDetailView):
    model = Shop

    def get(self, request, *args, **kwargs):
        shop_detail = Shop.objects.get(slug=self.kwargs['slug'])
        print(shop_detail)
        return HttpResponse(shop_detail)
