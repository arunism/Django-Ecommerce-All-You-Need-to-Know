from django.urls import path
from django.contrib.auth import views as auth_views
from customer import views
from customer.forms import MyPasswordResetForm

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reset/password/',
          auth_views.PasswordResetView.as_view(template_name='reset-password.html', form_class=MyPasswordResetForm),
          name='reset_password'
          ),
    path('reset/password/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='reset-password-done.html'),
          name='reset_password_done'
          ),
    path('me/', views.profile, name='profile'),
]
