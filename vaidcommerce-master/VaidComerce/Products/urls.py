from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('category/<name>/', views.get_category, name="category"),
    path('single/<int:id>/', views.get_single, name="single_product"),
    path('product_add/', views.get_productadd, name="product_add"),
    path('product_category_add/', views.get_category_add, name="product_category_add"),
    path('product_update/<int:id>/', views.get_update, name='product_update'),
    path('product_delete/<int:id>/', views.get_delete, name='product_delete'),
    path('product_data_table/', views.get_product_datatable, name="product_admin"),
    path('add_to_cart/<slug>/', views.get_add_to_cart, name="add_to_cart"),
    path('remove_form_cart/<slug>/', views.get_remove_form_cart, name="remove_form_cart"),
    path('order_summary_product/', views.get_order_summary, name="order_summary"),
    path('single_remove_form_cart/<slug>/', views.get_single_remove_form_cart, name="single_remove_form_cart"),
    path('orderitem/<int:id>/', views.get_orderitem, name="orderitem"),
    path('orderitem_delete/<int:id>/', views.get_orderitem_delete, name="orderitem_delete"),
    path('subcategory/', views.get_subcategory, name="subcategory"),
    path('checkout/', views.get_checkout, name="checkout"),
]