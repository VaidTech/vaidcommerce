from datetime import datetime
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from phone_field import PhoneField
LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger'),
)


class Category(models.Model):
    name        = models.CharField(max_length=120)

    def __str__(self):
        return self.name  


class subcategory(models.Model):
    categoryname    = models.ForeignKey(Category, on_delete=models.CASCADE)
    name            = models.CharField(max_length=120)
    

    def __str__(self):
        return self.name 
        

# Product Model 
class Product(models.Model):
    title       = models.CharField(max_length=120)
    categories  = models.ForeignKey(Category, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="upload")
    price       = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    label       = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    update      = models.DateTimeField(auto_now_add=False,auto_now=True)
   

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "slug") 

    
    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={
            'slug':self.slug
            })
    def get_remove_form_cart_url(self):
        return reverse('remove_form_cart', kwargs={
            'slug':self.slug
            })
    
    

class ImageGallery(models.Model):
    post     = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image_gallerys")
    image    = models.ImageField(upload_to="upload_to/", blank=True, null=True)

    def __str__(self):
        return self.post.title + "image"


    


# OrderItem
class OrderItem(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered     = models.BooleanField(default=False)
    item        = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_item_discount_price(self):
        return self.quantity * self.item.discount_price     

    def get_amount_save(self):
        return self.get_total_item_price() - self.get_total_item_discount_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()           

class Order(models.Model): 
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items       = models.ManyToManyField(OrderItem)
    start_date  = models.DateTimeField(auto_now_add=True)
    ordered_date= models.DateTimeField()
    order_verify= models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total    


class BillingAddress(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile_number  = PhoneField(blank=True, help_text='Contact phone number')
     

    def __str__(self):
        return self.user.username


class Token(models.Model):
    user_name      = models.CharField(max_length=120)
    tokenID      = models.IntegerField()
    used         = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

 





 


