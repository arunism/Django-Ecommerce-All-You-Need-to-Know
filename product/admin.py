from django.contrib import admin
from product.models import Product

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

admin.site.register(Product, ProductAdmin)
