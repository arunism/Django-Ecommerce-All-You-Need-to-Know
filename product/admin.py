from django.contrib import admin
from product.models import Product, Cart, Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['user', 'title', 'category']
    list_display = ['title', 'slug', 'discounted_price', 'created_at']
    # list_editable = ['new_price', 'available']
    list_filter = ['category', 'created_at']
    readonly_fields = ['slug', 'created_at', 'updated_at', 'rating', 'ratings_quantity']
    class Meta:
        model = Product

class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['product', 'user', 'quantity', 'created_at']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['user', 'created_at', 'updated_at', 'product', 'quantity', 'size', 'color']
    class Meta:
        model = Cart

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['id', 'user', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['user', 'profile', 'created_at', 'updated_at', 'product', 'quantity', 'size', 'color']
    class Meta:
        model = Order

admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
