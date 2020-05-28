from django.contrib.auth.models import User
from Products.models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver
from PaymentApp.models import Payment


@receiver(post_save, sender=Payment)
def updated_payment(instance, created, **kwargs):
	order = instance.user_order
	# print(order.order_verify)
	# print(instance.payment_verify)
	if instance.payment_verify == True:
		order.order_verify =True
		print(order.order_verify)
		order.save()
		
	elif instance.payment_verify == False:
		order.order_verify = False
		order.save()
	