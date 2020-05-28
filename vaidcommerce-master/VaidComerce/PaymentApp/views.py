from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Payment
from Products.models import Product, Order, BillingAddress
from .forms import PaymentForm
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages


User = get_user_model() 

# Create your views here.


def get_payment(request,id):
	order = get_object_or_404(Order, user=request.user, id=id)

	print(order.user)
	form = PaymentForm(request.POST or None)
	try:
	    order_active = Order.objects.get(user=request.user, order_verify=False)
	    if request.method =='POST':
	    	if form.is_valid():
	    		user_order = order
	    		payment_method = form.cleaned_data.get('payment_method')
	    		email = form.cleaned_data.get('email')
	    		mobile_number = form.cleaned_data.get('mobile_number_0')
	    		transaction = form.cleaned_data.get('transaction')
	    		time = form.cleaned_data.get('time')
	    		amount = form.cleaned_data.get('amount')
	    		print(user_order)
	    		payment_create = Payment(
					user_order = user_order,
                    payment_method = payment_method,
                    email = email,
                    mobile_number = mobile_number,
                    transaction = transaction,
                    time = time,
                    amount = amount
					)
	    		payment_create.save()
	    		messages.success(request, 'Payment success')
	    		return redirect('index')		
	except:
		messages.info(request, 'Payment not success')
		return redirect('index')


	context = {
		'form':form,
		'order':order,
		
	}		
	return render(request, 'payment/payment.html', context)



