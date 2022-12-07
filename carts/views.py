from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from store.models import Product
from .models import Cart, CartItem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) # get the product
    print(product)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using cart id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            quantity=1,
            product=product,
            cart=cart
        )
        cart_item.save()
    return redirect('cart')

def remove_cart_item(request, product_id):
    product = Product.objects.get(id=product_id) # get the product
    # print(product)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using cart id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        print(cart_item.quantity)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            CartItem.objects.get(product=product, cart=cart).delete()
        
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

def remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id) # get the product
    cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using cart id
    try:
        CartItem.objects.get(product=product, cart=cart).delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_item=None):
    cart_session = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.filter(cart=cart_session, is_active=True)

    try:
        for item in cart_item:
            # product = Product.objects.get(pr = cart_item.product)
            total += (item.product.price * item.quantity)
            quantity += item.quantity
    except ObjectNotExist:
        pass
    context = {
        'total':total,
        'quantity': quantity,
        'cart_items':cart_item
    }

    return render(request, 'store/cart.html', context)