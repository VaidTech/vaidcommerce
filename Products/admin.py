from django.contrib import admin
from .models import Product, Category, OrderItem, Order, Token, ImageGallery, subcategory, BillingAddress
# Register your models here.ImageGallery, 

admin.site.register(Product)

admin.site.register(Category)

admin.site.register(OrderItem)

admin.site.register(Order)

admin.site.register(ImageGallery)

admin.site.register(Token)

admin.site.register(subcategory)

admin.site.register(BillingAddress)