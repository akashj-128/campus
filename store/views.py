from django.shortcuts import render,get_object_or_404
from .models import Product
from .models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger ,Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = Product.objects.filter(is_available=True).order_by('id')

    # Filter by category if given
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=categories)

    # Price filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
            products = products.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass  # ignore invalid input

    # Pagination
    paginator = Paginator(products, 9)  # 9 products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
        'min_price': request.GET.get('min_price', '0'),
        'max_price': request.GET.get('max_price', '5000'),
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product = single_product).exists()
    except Exception as e: 
        raise e
    
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
    }

    return render(request, 'store/product_detail.html',context)

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product

def search(request):
    keyword = request.GET.get('keyword', '').strip()

    if keyword == "":
        return redirect('store')

    products = Product.objects.order_by('-created_date').filter(
        Q(description__icontains=keyword) |
        Q(product_name__icontains=keyword)
    )

    context = {
        'products': products,
        'product_count': products.count(),
    }
    return render(request, 'store/store.html', context)

