from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request, category_slug=None):
    category_page = None
    products_list = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)


    return render(request, 'home.html', {'category': category_page, 'products': products})


def productPage(request):
    return render(request, 'product.html',)
