from django import forms
from django.contrib.auth import get_user_model
from .models import Product, Category, OrderItem, Order, subcategory, BillingAddress
User = get_user_model()




class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'categories',
            'image',
            'price',
            'discount_price',
            'label',
            'slug',
            'description',
            
        ]

class ProductCategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
         'user',
         'ordered',
         'item',
         'quantity'
        ]
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = subcategory
        fields = [
         'categoryname',
         'name',
    ]

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = [
          'mobile_number',
        ]    