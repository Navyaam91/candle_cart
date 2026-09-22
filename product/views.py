from django.shortcuts import render,redirect
# from . models import Product, Category, Review
# from .forms import ReviewForm
# from django.contrib import messages
# from customers.models import Customer
# from django.core.paginator import Paginator

def index(request):
    # shop=Product.objects.filter(deleted_at=Product.LIVE).order_by('-priority')[:3]
    return render(request, 'index.html')
def shop(request):
    # shop=Product.objects.filter(deleted_at=Product.LIVE).order_by('-priority')
    # paginator = Paginator(shop, 6)  # Show 6 products per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')
