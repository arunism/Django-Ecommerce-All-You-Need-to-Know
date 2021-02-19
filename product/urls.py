from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('product/details/<str:slug>/', views.ProductDetailView.as_view(), name='product_details'),
    path('add/to/cart/<str:slug>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
]
