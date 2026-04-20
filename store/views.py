from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product
from .forms import ProductForm


# ── helpers ──────────────────────────────────────────────────────────────────

def _base_ctx(request):
    """Common context injected into every public view."""
    return {'categories': Category.objects.all()}


# ── public views ─────────────────────────────────────────────────────────────

def home(request):
    ctx = _base_ctx(request)
    ctx['latest_products'] = Product.objects.select_related('category').all()[:12]
    return render(request, 'store/home.html', ctx)


def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products_list = Product.objects.filter(category=category).select_related('category')
    query = request.GET.get('q', '')
    if query:
        products_list = products_list.filter(name__icontains=query)
    paginator = Paginator(products_list, 12)
    products = paginator.get_page(request.GET.get('page'))
    ctx = _base_ctx(request)
    ctx.update({'category': category, 'products': products, 'query': query})
    return render(request, 'store/category.html', ctx)


def all_products(request):
    products_list = Product.objects.select_related('category').all()
    query = request.GET.get('q', '')
    cat_filter = request.GET.get('category', '')
    if query:
        products_list = products_list.filter(name__icontains=query)
    if cat_filter:
        products_list = products_list.filter(category__id=cat_filter)
    paginator = Paginator(products_list, 12)
    products = paginator.get_page(request.GET.get('page'))
    ctx = _base_ctx(request)
    ctx.update({'products': products, 'query': query, 'cat_filter': cat_filter})
    return render(request, 'store/all_products.html', ctx)


def contact(request):
    return render(request, 'store/contact.html', _base_ctx(request))


# ── auth views ────────────────────────────────────────────────────────────────

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('home')
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user and user.is_staff:
            login(request, user)
            return redirect(request.GET.get('next', 'home'))
        messages.error(request, 'Invalid credentials or not an admin account.')
    return render(request, 'store/admin_login.html', _base_ctx(request))


def admin_logout(request):
    logout(request)
    return redirect('home')


# ── admin product CRUD ────────────────────────────────────────────────────────

@login_required(login_url='admin_login')
def product_add(request):
    if not request.user.is_staff:
        return redirect('home')
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully.')
        return redirect('all_products')
    ctx = _base_ctx(request)
    ctx.update({'form': form, 'form_title': 'Add New Product', 'btn_label': 'Add Product'})
    return render(request, 'store/product_form.html', ctx)


@login_required(login_url='admin_login')
def product_edit(request, product_id):
    if not request.user.is_staff:
        return redirect('home')
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'"{product.name}" updated successfully.')
        return redirect('all_products')
    ctx = _base_ctx(request)
    ctx.update({'form': form, 'product': product,
                'form_title': f'Edit — {product.name}', 'btn_label': 'Save Changes'})
    return render(request, 'store/product_form.html', ctx)


@login_required(login_url='admin_login')
def product_delete(request, product_id):
    if not request.user.is_staff:
        return redirect('home')
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        name = product.name
        product.delete()
        messages.success(request, f'"{name}" deleted.')
        return redirect('all_products')
    ctx = _base_ctx(request)
    ctx['product'] = product
    return render(request, 'store/product_confirm_delete.html', ctx)
