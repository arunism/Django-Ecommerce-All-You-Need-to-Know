from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'title': 'Home', 'subtitle':'Products'}
    return render(request, 'index.html', context)
