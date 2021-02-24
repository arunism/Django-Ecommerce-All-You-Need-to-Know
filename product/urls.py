from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/list/', views.ProductListView.as_view(), name='product_list'),
    path('products/list/most/popular/', views.LatestProducts.as_view(), name='popular_products'),
    path('products/list/most/sold/', views.MostSoldProducts.as_view(), name='most_sold_products'),
    path('products/list/low/price/', views.LowPriceProducts.as_view(), name='low_price_products'),
    path('products/list/medium/price/', views.MediumPriceProducts.as_view(), name='medium_price_products'),
    path('products/list/high/price/', views.HighPriceProducts.as_view(), name='high_price_products'),
    path('product/details/<str:slug>/', views.ProductDetailView.as_view(), name='product_details'),
    path('add/to/cart/<str:slug>', views.add_to_cart, name='add_to_cart'),
    path('update/cart/<str:slug>', views.update_quantity, name='update_quantity'),
    path('remove/from/cart/<str:slug>', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]
