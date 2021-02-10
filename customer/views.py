from django.shortcuts import render

# Create your views here.

def register(request):
    context = {'title':'Register', 'subtitle':'User'}
    return render(request, 'register.html', context)

def login(request):
    context = {'title':'Login', 'subtitle':'User'}
    return render(request, 'login.html', context)

def profile(request):
    context = {'title':'Profile', 'subtitle':'User'}
    return render(request, 'my-account.html', context)
