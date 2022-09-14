from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total_customers = customer.count()
    total_orders = Order.objects.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customer,
    'total_orders':total_orders, 'delivered':delivered,
    'pending':pending}

    return render(request, 'account/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'account/products.html', {'products':products})


def customer(request):
    return render(request, 'account/customer.html')