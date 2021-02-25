from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from product.models import Product, Cart, Order, Contact
from customer.models import Profile, Review

# Create your views here.

def home(request):
    product = Product.objects.all().order_by('-created_at')
    new_releases = product[:10]
    featured_products = [items for items in product if items.rating > 4.5]
    featured_products = featured_products[:10]
    reviews = Review.objects.filter(service='Excellent')[:10]
    context = {'title': 'Home',
                'subtitle':'Products',
                'new_releases':new_releases,
                'featured_products':featured_products,
                'reviews':reviews
                }
    return render(request, 'index.html', context)

def pagination_func(request, product):
    paginate = Paginator(product, 12)
    page_num = request.GET.get('page', 1)
    try:
        page = paginate.page(page_num)
    except EmptyPage:
        page = paginate.page(1)
    return page

class ProductListView(View):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        Cosmetics_and_beauty = Product.objects.filter(category='Cosmetics_and_beauty')
        kids_clothes = Product.objects.filter(category='kids_clothes')
        men_and_women_clothes = Product.objects.filter(category='men_and_women_clothes')
        gadgets_accessories = Product.objects.filter(category='gadgets_accessories')
        electronics = Product.objects.filter(category='electronics')
        # PAGINATION STARTS HERE
        page = pagination_func(request, product)
        # PAGINATION ENDS HERE
        context = {'title':'Latest Releases',
                    'subtitle':'Products',
                    'products': page,
                    'kids_clothes':kids_clothes,
                    'men_and_women_clothes': men_and_women_clothes,
                    'gadgets_accessories': gadgets_accessories,
                    'electronics': electronics,
                }
        return render(request, 'product-list.html', context)

class LatestProducts(View):
    def get(self, request):
        product = Product.objects.all().order_by('-rating', '-created_at')
        # PAGINATION STARTS HERE
        page = pagination_func(request, product)
        # PAGINATION ENDS HERE
        context = {'sort_title':'Most Popular',
                    'subtitle':'Products',
                    'products': page,
                }
        return render(request, 'product-list.html', context)

class MostSoldProducts(View):
    def get(self, request):
        product = Product.objects.all().order_by('-ratings_quantity', '-created_at')
        # PAGINATION STARTS HERE
        page = pagination_func(request, product)
        # PAGINATION ENDS HERE
        context = {'sort_title':'Most Sale',
                    'subtitle':'Products',
                    'products': page,
                }
        return render(request, 'product-list.html', context)

class LowPriceProducts(View):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        page = [items for items in product if int(items.discounted_price) <= 10]
        # PAGINATION STARTS HERE
        page = pagination_func(request, page)
        # PAGINATION ENDS HERE
        context = {'price_title':'Low Price (< $10)',
                    'subtitle':'Products',
                    'products': page,
                }
        return render(request, 'product-list.html', context)

class MediumPriceProducts(View):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        page = [items for items in product if int(items.discounted_price) > 10 and int(items.discounted_price) <= 30]
        # PAGINATION STARTS HERE
        page = pagination_func(request, page)
        # PAGINATION ENDS HERE
        context = {'price_title':'Medium Price ($10 - $30)',
                    'subtitle':'Products',
                    'products': page,
                }
        return render(request, 'product-list.html', context)

class HighPriceProducts(View):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        page = [items for items in product if int(items.discounted_price) > 30]
        # PAGINATION STARTS HERE
        page = pagination_func(request, page)
        # PAGINATION ENDS HERE
        context = {'price_title':'High Price (> $30)',
                    'subtitle':'Products',
                    'products': page,
                }
        return render(request, 'product-list.html', context)

class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        context = {'sort_title':'Details', 'subtitle':'Products', 'product':product}
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
def increase_quantity(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    cart = Cart.objects.get(user=user, product=product)
    cart.quantity += 1
    cart.save()
    return redirect('product:cart')

@login_required
def decrease_quantity(request, slug):
    user = request.user
    product = Product.objects.get(slug=slug)
    cart = Cart.objects.get(user=user, product=product)
    cart.quantity -= 1
    cart.save()
    if cart.quantity == 0:
        cart.delete()
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

def checkout(request):
    user = request.user
    profile = Profile.objects.filter(user=user).order_by('-created_at')
    profile = profile[0]
    cart = Cart.objects.filter(user=user)

    amount = 0.00
    shipping_charge = 1.50
    for item in cart:
        each_total = float(item.product.discounted_price) * item.quantity
        amount += each_total
    total_amount = amount + shipping_charge

    context = {
                'title':'Checkout',
                'subtitle':'Products',
                'profile':profile,
                'cart': cart,
                'amount': round(amount, 2),
                'shipping_charge': round(shipping_charge, 2),
                'total_amount': round(total_amount, 2)
            }
    return render(request, 'checkout.html', context)

def order_placed(request):
    user = request.user
    profile = Profile.objects.filter(user=user).order_by('-created_at')
    profile = profile[0]
    cart = Cart.objects.filter(user=user)

    for item in cart:
        order = Order(user=user, profile=profile, product=item.product, quantity=item.quantity)
        order.save()
        item.delete()
    return redirect('product:orders')

def orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    context = {'title':'Orders', 'subtitle':'Products', 'orders':orders}
    return render(request, 'order.html', context)

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
    # PAGINATION STARTS HERE
    page = pagination_func(request, product)
    # PAGINATION ENDS HERE
    context = {'title':'Search Results', 'subtitle':'Products', 'products':page}
    return render(request, 'product-list.html', context)

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks for your response! We will get back to you soon.')

        return redirect('product:contact')
    else:
        context = {'title':'Contact'}
        return render(request, 'contact.html', context)
