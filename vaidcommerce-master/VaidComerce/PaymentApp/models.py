from datetime import datetime
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from phone_field import PhoneField
from Products.models import Order

PAYMENT_CHOICES = (
    ('BKASH','bkash'),
    ('ROCKET','rocket'),
    ('BANK','bank'),
)
 
class Payment(models.Model):
	user_order       = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
	payment_method   = models.CharField(choices=PAYMENT_CHOICES, blank=False, null=False, max_length=120)
	email            = models.EmailField()
	mobile_number    = PhoneField(blank=True, help_text='Contact phone number')
	transaction      = models.CharField(unique=True, max_length=100) 
	time             = models.TimeField(blank=True, null=True)
	amount           = models.FloatField(blank=True, null=True)
	payment_verify   = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user_order)





