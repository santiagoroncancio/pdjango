from django.shortcuts import render,redirect
from .models import Cart
from .utils import get_or_create_cart
from products.models import Product

def cart(request):
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html',{
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(product)

    return render(request, 'carts/add.html',{
        'product':product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')