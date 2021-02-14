from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from customer.forms import MyPasswordChangeForm, MyPasswordResetForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Oops! User with this Username already exists.')
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Oops! User with this Email already exists.')
                return redirect('user:register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, f'Congratulations! {first_name}, Your account has been created! Now, please login and edit your informations.')
                return redirect('user:profile')
        else:
            messages.error(request, 'Oops! Password fields do not match.')
            return redirect('user:register')
    else:
        context = {'title':'Register', 'subtitle':'User'}
        return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been logged in to your account!')
            return redirect('product:product_list')
        else:
            messages.error(request, 'Oops! Username and Password do not match!')
            return redirect('user:login')
    else:
        context = {'title':'Login', 'subtitle':'User'}
        return render(request, 'login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out of your account!')
    return redirect('user:login')


@login_required
def profile(request):
    # Change User Password
    if request.method == 'POST':
        form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # This will update the session and we won't be logged out after changing the password
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been updated!')
            return redirect('user:profile')
        else:
            messages.success(request, 'Oops! Something went wrong. Please try again.')
            return redirect('user:profile')
    else:
        form = MyPasswordChangeForm(user=request.user)
    context = {'title':'Profile',
               'subtitle':'User',
               'change_password_form':form,
               }
    return render(request, 'my-account.html', context)
