from asgiref.sync import sync_to_async
import asyncio
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from cart.forms import CartAddProductForm
from .models import Product, Category


def shop_list(request, category_slug=None):
    category = None
    categories = asyncio.run(get_categories_async())
    products = asyncio.run(get_products_async())
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    data = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_product_form': cart_product_form

    }
    return render(request=request, template_name='shop/index.html', context=data)


def shop_detail(request, id, slug):
    product = asyncio.run(get_product_by_id_async(id, slug))
    categories = asyncio.run(get_categories_async())
    cart_product_form = CartAddProductForm()
    data = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request=request, template_name='shop/detail.html', context=data)


class RegisterUserForm(FormView):
    form_class = UserCreationForm
    template_name = "shop/register.html"
    success_url = reverse_lazy('shop:login')
    categories = Category.objects.all()
    extra_context = {'categories': categories}

    def form_valid(self, form):
        form.save()
        return super(RegisterUserForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterUserForm, self).form_invalid(form)


class LoginUserForm(LoginView):
    form_class = AuthenticationForm
    template_name = "shop/login.html"

    def get_success_url(self):
        return reverse_lazy('shop:shop_list')

    categories = Category.objects.all()
    extra_context = {'categories': categories}

    def form_valid(self, form):
        return super(LoginUserForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginUserForm, self).form_invalid(form)


def logout_user(request):
    logout(request)
    return redirect('shop:shop_list')


@sync_to_async
def get_product_by_id_async(pk, slug):
    product = Product.objects.get(pk=pk, slug=slug)
    return product


@sync_to_async
def get_products_async():
    products = Product.objects.all()
    return products

@sync_to_async
def get_categories_async():
    categories = Category.objects.all()
    return categories