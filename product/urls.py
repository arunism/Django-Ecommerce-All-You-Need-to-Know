from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
]
