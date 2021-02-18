from django.contrib import admin
from customer.models import Profile, Review

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['user', 'district', 'street']
    list_display = ['user', 'phone', 'gender', 'created_at']
    list_filter = ['created_at', 'state', 'district', 'street']
    readonly_fields = ['user', 'created_at', 'updated_at', 'phone', 'gender', 'country', 'state', 'district', 'city', 'street']

admin.site.register(Review)
