from django.urls import path
from customer import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('my/profile/', views.profile, name='profile'),
]
