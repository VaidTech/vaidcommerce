from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
	
	class Meta:
		model = Payment
		fields = [
		   'user_order',
         'payment_method',
         'email',
         'mobile_number',
         'transaction',
         'time',
         'amount'

		]