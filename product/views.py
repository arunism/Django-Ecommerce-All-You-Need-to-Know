from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from product.models import Product, Cart, Order
from customer.models import Review

# Create your views here.

def home(request):
    new_releases = Product.objects.all().order_by('-created_at')[:10]
    featured_products = Product.objects.filter(rating=4.5).order_by('-created_at')[:10]
    reviews = Review.objects.filter(service='Excellent')[:10]
    context = {'title': 'Home',
                'subtitle':'Products',
                'new_releases':new_releases,
                'featured_products':featured_products,
                'reviews':reviews
                }
    return render(request, 'index.html', context)

class ProductListView(View):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        Cosmetics_and_beauty = Product.objects.filter(category='Cosmetics_and_beauty')
        kids_clothes = Product.objects.filter(category='kids_clothes')
        men_and_women_clothes = Product.objects.filter(category='men_and_women_clothes')
        gadgets_accessories = Product.objects.filter(category='gadgets_accessories')
        electronics = Product.objects.filter(category='electronics')
        context = {'title':'Products',
                    'products': product,
                    'kids_clothes':kids_clothes,
                    'men_and_women_clothes': men_and_women_clothes,
                    'gadgets_accessories': gadgets_accessories,
                    'electronics': electronics,
                }
        return render(request, 'product-list.html', context)

class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        context = {'title':'Details', 'subtitle':'Products', 'product':product}
        return render(request, 'product-detail.html', context)

@login_required
def add_to_cart(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    cart = Cart(user=user, product=product)
    if Cart.objects.filter(user=user, product=product).exists():
        cart.quantity += 1
    else:
        cart.save()
    return redirect('product:cart')

@login_required
def remove_from_cart(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    cart = Cart.objects.filter(user=user, product=product)
    cart.delete()
    return redirect('product:cart')

@login_required
def update_quantity(request, slug, quantity):
    user = request.user
    product = Product.objects.get(slug=slug)
    cart = Cart.objects.filter(user=user, product=product)
    if int(quantity) == 0:
        cart.delete()
    else:
        cart.quantity == quantity
        cart.save()
    return redirect('product:cart')

@login_required
def cart(request):
    amount = 0.00
    shipping_charge = 1.50

    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        for item in cart:
            each_total = float(item.product.discounted_price) * item.quantity
            amount += each_total
        total_amount = amount + shipping_charge

        request.session['cart_items_count'] = cart.count()
    context = {
                'title':'Cart',
                'subtitle':'Products',
                'cart':cart,
                'amount':round(amount, 2),
                'shipping_charge':round(shipping_charge, 2),
                'total_amount':round(total_amount, 2),
            }
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

def search(request):
    try:
        query = request.GET.get('query')
    except:
        query = None
    if query:
        product = Product.objects.all()
        product = product.filter(Q(title__icontains=query) | Q(category__icontains=query))
    else:
        product = Product.objects.all().order_by('-created_at')
    context = {'title':'Search Results', 'subtitle':'Products', 'products':product}
    return render(request, 'product-list.html', context)

def contact(request):
    context = {'title':'Contact'}
    return render(request, 'contact.html', context)
