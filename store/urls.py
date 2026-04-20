from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.all_products, name='all_products'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('contact/', views.contact, name='contact'),
    
    # Admin auth
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    
    # Admin product management
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:product_id>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
