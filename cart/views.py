from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 value=cd['value'],
                 update_value=cd['update'])
    return redirect('cart:show_cart')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:show_cart')


def show_cart(request):
    cart = Cart(request)
    categories = Category.objects.all()
    data = {
        'cart': cart,
        'categories': categories
    }
    for item in cart:
        item['update_value_form'] = CartAddProductForm(initial={'value': item['value'],
                                                                'update': True})
    return render(request, 'cart/cart.html', context=data)
