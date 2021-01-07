from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def slide_view(request):
    return render(request,'homepage/home_page.html',context={})