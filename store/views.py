from django.shortcuts import render

# Create your views here.
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    if category_slug is not None:
        products = Product.objects.filter(is_available=True, category__slug=category_slug)
    else:
        products = Product.objects.filter(is_available=True)

    context = {
        'products': products,
        'links': Category.objects.all()
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product
    }

    return render(request, 'store/product_detail.html', context)