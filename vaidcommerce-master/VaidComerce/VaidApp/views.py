from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from.forms import registerUserForm, TokenForm
User = get_user_model() 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q  

from Products.models import Product, Token, Category 


def get_index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    search = request.GET.get('q')
    if search:
        product = product.filter(
            Q(title__icontains=search) | Q(price__contains=search)
        )
    paginator = Paginator(product, 3) # Show 3 contacts per page.

    page_number = request.GET.get('page')
    total_product = paginator.get_page(page_number)
    
    context ={
        'product':product,
        'category':category,
        'product':total_product
    }
    return render(request, "home.html", context)
   

def get_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            user        = request.POST.get('user')
            password    = request.POST.get('pass')
            auth = authenticate(username=user, password=password)
            if auth:
                login(request, auth)
                return redirect("login")        
    return render(request, "login.html") 

# @login_required(login_url="/")
def get_logout(request):
    logout(request)
    return redirect("index")

import random as r
def get_register(request):
    form = registerUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_active = False
            instance.save() 

            token = r.randint(0,9999)
            print(type(token))
            create_token = Token.objects.create(user_name=instance.username, tokenID=token)
            create_token.save()
          
            domain = get_current_site(request)
            mail_subject = "Confirmation Messages"
            message = render_to_string('confirm_email.html',{
                'user':instance,
                'domain':domain,
                'uid':instance.id,
                "token": token, 
            })
            to_email = form.cleaned_data.get('email') # instance.email
            to_list = [to_email,]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
            return HttpResponse("<h1> Thanks for your Registration.A Confirmation link was sent to your email  </h1>")
    
    context ={
        'form':form
        }    
    return render(request, "Register.html", context)

 
def get_activate(request, uidb64, token):
    try:
        user = get_object_or_404(User, pk=uidb64)
    except:
        raise Http404("Not user found")
    if user is not None:
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponse("<h2> Account is activated. Please Verify  <a href='/verify'> Verify </a> </h2>")
    else:
        return HttpResponse("<h2>The link is invalid </h2>")


def get_verify(request):
    try:
        form = TokenForm(request.POST or None)
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            user_token = request.POST.get('tokenID')
            token = get_object_or_404(Token, user_name=user_name, tokenID=user_token, used=False)
            print(token)
            if token:
                token.used=True
                token.save()
                return HttpResponse("<h3>Success Full Verify</h3>")
             
    except:
        raise Http404(" Token invalid ") 
    context ={
        'form':form
    }    
    return render(request, "verify.html", context)
    

 



 
