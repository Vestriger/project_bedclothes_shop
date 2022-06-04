from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def shop_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    data = {
        'category': category,
        'categories': categories,
        'products': products

    }
    return render(request=request, template_name='shop/index.html', context=data)


def shop_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    categories = Category.objects.all()
    data = {
        'product': product,
        'categories': categories
    }
    return render(request=request, template_name='shop/detail.html', context=data)

