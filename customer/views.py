from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from customer.forms import MyPasswordChangeForm, MyPasswordResetForm, ProfileForm
from customer.models import Profile
from customer.utils import login_excluded

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
                return redirect('user:update_profile')
        else:
            messages.error(request, 'Oops! Password fields do not match.')
            return redirect('user:register')
    else:
        context = {'title':'Register', 'subtitle':'User'}
        return render(request, 'register.html', context)


@login_excluded('user:profile')
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
    context = {'title':'Profile',
               'subtitle':'User',
               }
    return render(request, 'dashboard.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            user = request.user
            gender = profile_form.cleaned_data['gender']
            phone = profile_form.cleaned_data['phone']
            country = profile_form.cleaned_data['country']
            state = profile_form.cleaned_data['state']
            district = profile_form.cleaned_data['district']
            city = profile_form.cleaned_data['city']
            street = profile_form.cleaned_data['street']

            profiles = Profile(user=user,phone=phone,gender=gender,country=country,state=state,district=district,city=city,street=street)
            profiles.save()
            messages.success(request, 'Congratulations! Your profile has been updated.')
        else:
            messages.error(request, "Oops! Your profile couldn't be updated. Please try again.")
            return redirect('user:update_profile')

    else:
        profile_form = ProfileForm()

    context = {'title':'Change Password',
               'subtitle':'User',
               'profile_form':profile_form,
               'address':address,
               }
    return render(request, 'update-profile.html', context)


@login_required
def address(request):
    address = Profile.objects.filter(user=request.user).order_by('-created_at')[:2]
    context = {'title':'Address',
               'subtitle':'User',
               'address':address,
               }
    return render(request, 'address.html', context)

@login_required
def payment(request):
    context = {'title':'Payment Method',
               'subtitle':'User',
               }
    return render(request, 'payment.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        change_password_form = MyPasswordChangeForm(user=request.user, data=request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            # This will update the session and we won't be logged out after changing the password
            update_session_auth_hash(request, change_password_form.user)
            messages.success(request, 'Your password has been updated!')
            return redirect('user:update_profile')
        else:
            messages.success(request, 'Oops! Something went wrong. Please try again.')
            return redirect('user:update_profile')
    else:
        change_password_form = MyPasswordChangeForm(user=request.user)
    context = {'title':'Change Password',
               'subtitle':'User',
               'change_password_form':change_password_form,
               }
    return render(request, 'change-password.html', context)
