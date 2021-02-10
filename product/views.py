from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'title': 'Home', 'subtitle':'Products'}
    return render(request, 'index.html', context)

def product_list(request):
    context = {'title':'Products'}
    return render(request, 'product-list.html', context)

def product_details(request):
    context = {'title':'Details', 'subtitle':'Products'}
    return render(request, 'product-detail.html', context)

def cart(request):
    context = {'title':'Cart', 'subtitle':'Products'}
    return render(request, 'cart.html', context)

def wishlist(request):
    context = {'title':'Wishlist', 'subtitle':'Products'}
    return render(request, 'wishlist.html', context)

def orders(request):
    context = {'title':'Orders', 'subtitle':'Products'}
    return render(request, 'my-account.html', context)

def checkout(request):
    context = {'title':'Checkout', 'subtitle':'Products'}
    return render(request, 'checkout.html', context)

def contact(request):
    context = {'title':'Contact'}
    return render(request, 'contact.html', context)
