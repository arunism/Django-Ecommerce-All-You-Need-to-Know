from django.urls import path
from django.contrib.auth import views as auth_views
from customer import views
from customer.forms import MyPasswordResetForm, MySetPasswordForm

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
          auth_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'),
          name='password_reset_done'
          ),
    path('reset/password/confirm/<uid64>/<token>',
          auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html', form_class=MySetPasswordForm),
          name='password_reset_confirm'
          ),
    path('reset/password/complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),
          name='password_reset_complete'
          ),
    path('me/', views.profile, name='profile'),
    path('update/profile/', views.update_profile, name='update_profile'),
    path('address/', views.address, name='address'),
    path('payment/', views.payment, name='payment'),
    path('change/password/', views.change_password, name='change_password'),
]
