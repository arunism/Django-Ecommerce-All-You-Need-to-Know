from django.urls import path
from django.contrib.auth import views as auth_views
from customer import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('me/', views.profile, name='profile'),
]
