from django.shortcuts import render,redirect
from django.http import HttpResponse
from listings.models import Produkt
from . models import Cart,CartItem
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request):
    return render(request,'cart/cart.html')

def add_cart(request,product_id):
    product = Produkt.objects.get(id=product_id)
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request)) #get cart using session id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,quantity=1,cart=cart)
    cart_item.save()
    return HttpResponse(cart_item.product)
    exit()
    return redirect('cart')