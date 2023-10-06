from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator


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

    shop_search_input = request.GET.get('shop_search')
    category_filter = request.GET.get('category_filter')
    color_filter = request.GET.get('color_filter')
    size_filter = request.GET.get('size_filter')
    # start_date = request.GET.get('start_date')
    # end_date = request.GET.get('end_date')
    # category_id = request.GET.get('category')

    # Initial filters with Q()
    filters = Q()

    if shop_search_input:
        filters &= Q(name__icontains=shop_search_input)

    if category_filter:
        # filtered_data = ProductCategory.objects.filter(title=category_filter)
        filters &= Q(category=category_filter)
    
    if color_filter:
        filters &= Q(color=color_filter)
    
    if size_filter:
        filters &= Q(size=size_filter)
    # else:
    #     filtered_data = ProductCategory.objects.all()

    # if start_date:
    #     if not end_date:
    #         end_date = timezone.now().date()
    #     filters &= Q(created_at__date__range=[start_date, end_date])

    # if category_id:
    #     filters &= Q(category=category_id)

    # Fetch the news based on built filters
    products = Product.objects.filter(filters) if filters else Product.objects.all()

    product_count = products.count()

    # Pagination
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    page_products = paginator.get_page(page)


    context = {
        'title' : 'Ogani Shop',
        'departments' : ProductCategory.objects.all(),
        'latest_products' : Product.objects.all().order_by('-created_at'),
        'all_products' : page_products,
        'product_count' : product_count,
        'discount_objects' : Discount_Product.objects.all(),
        'colors' : Colors.objects.all(),
        'sizes' : Size.objects.all(),
        'search_input' : shop_search_input if shop_search_input else '',
        # 'products' : page_products,

        # 'filtered_data' : filtered_data,

    }

    return render(request, 'shop-grid.html', context)

def blog(request):
    blog_search_input = request.GET.get('blog_search')
    if blog_search_input is not None and blog_search_input != '':
        blogs = Blog.objects.filter(title__icontains=blog_search_input)
    else:
        blogs = Blog.objects.all()

    context = {
        'title': 'Ogani Blog',
        'departments': ProductCategory.objects.all(),
        'blogs': blogs,
        'search_input' : blog_search_input if blog_search_input else '',
        'recent': Blog.objects.all().order_by('-created_at')
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