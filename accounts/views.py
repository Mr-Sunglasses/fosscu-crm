from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html')

def product(request):
    return render(request, 'accounts/products.html')
