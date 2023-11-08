from django.shortcuts import render

def cart(request):
    return render(request, 'cart/cart.html')

def wishlist(request):
    return render(request, 'cart/wishlist.html')