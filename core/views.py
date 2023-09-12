from django.shortcuts import redirect, render
from django.http import HttpResponse


from core.forms import ContactForm
from core.models import (Blog, Product, Settings, ProductCategory, 
                         BlogCategory, Discount_Product, Colors, Size,

)

# Create your views here.

def index(request):
    context = {
        'title' : 'Ogani Home',
        'blogs' : Blog.objects.all().order_by('-created_at'),
        'featureds' : Product.objects.all().order_by('-created_at'),
        'latest_products' : Product.objects.all().order_by('-created_at'),
        'toprated_products' : Product.objects.all().order_by('heart'),
        'review_products' : Product.objects.all().order_by('-price'),
        'departments' : ProductCategory.objects.all(),

    }

    return render(request, 'index.html', context)

def shop(request):
    context = {
        'title' : 'Ogani Shop',
        'departments' : ProductCategory.objects.all(),
        'latest_products' : Product.objects.all().order_by('-created_at'),
        'all_products' : Product.objects.all(),
        'product_count' : Product.objects.count(),
        'discount_objects' : Discount_Product.objects.all(),
        'colors' : Colors.objects.all(),
        'sizes' : Size.objects.all(),

    }

    return render(request, 'shop-grid.html', context)

def blog(request):
    context = {
        'title' : 'Ogani Blog',
        'departments' : BlogCategory.objects.all(),
        'blogs' : Blog.objects.all(),
        'recent' : Blog.objects.all().order_by('-created_at')

    }

    return render(request, 'blog.html', context)

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    
    
    context = {
        'title' : 'Ogani Contact',
        'departments' : ProductCategory.objects.all(),
        'form' : form,    
    }

    return render(request, 'contact.html', context)

def shop_details(request, slug):
    context = {
        'title' : ' Ogani Shop Details',
        'departments' : ProductCategory.objects.all(),
        'related_products' : Product.objects.all().order_by('-created_at'),
        'details' : Product.objects.get(slug=slug),

    }

    return render(request, 'shop-details.html', context)

def blog_details(request, slug):
    context = {
        'title' : 'Ogani Blog Details',
        'blogs' : Blog.objects.all().order_by('-created_at'),
        'departments' : ProductCategory.objects.all(),
        'blog_categories' : BlogCategory.objects.all(),
        'details' : Blog.objects.get(slug=slug),
    }

    return render(request, 'blog-details.html', context)

def checkout(request):
    context = {
        'title' : 'Ogani Checkout',
        'departments' : ProductCategory.objects.all(),
    }

    return render(request, 'checkout.html', context)

def shopping_cart(request):
    context = {
        'title' : 'Ogani Shopping Cart',
        'departments' : ProductCategory.objects.all(),
    }

    return render(request, 'shoping-cart.html', context)


def discount_details(request, slug):
    context = {
        'title' : 'Ogani Discount Details',
        'details' : Discount_Product.objects.get(slug=slug),
        'related_products' : Product.objects.all().order_by('-created_at'),
    }

    return render(request, 'discount_details.html', context)


def departments(request,slug):
    context = {
        'title' : 'Deparments',
        'products' : Product.objects.all(),
        'details' : ProductCategory.objects.get(slug=slug),
        'latest_products' : Product.objects.all().order_by('-created_at'),
        'departments' : ProductCategory.objects.all()
    }

    return render(request, 'departments.html', context)