from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def all_household(request):
    products = Product.objects.filter(category='Household')
    return render(request,"products/all_household.html", {'products': products})