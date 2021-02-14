from django.shortcuts import render
from django.views import View
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
