from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category, ImageGallery, OrderItem, Order, subcategory, BillingAddress
from .forms import ProductAddForm,ProductCategoryAddForm, OrderItemForm, SubcategoryForm, CheckOutForm
from django.forms import modelformset_factory
from django.core.paginator import Paginator 
from django.utils import timezone


def get_category(request, name):
     
    category = get_object_or_404(Category, name=name)
    posts = Product.objects.filter(categories=category.id)
    subcategory = category.subcategory_set.all()
    print(subcategory)    
    context ={ 
        'posts':posts,
        'category':category,
        'subcategory':subcategory   
    }
    return render(request, 'category.html', context)



def get_single(request, id):
    post = get_object_or_404(Product, id=id)
    gallery = post.image_gallerys.all()
    print(gallery)
    related = Product.objects.filter(categories=post.categories).exclude(id=id)[:4] 
    
    context = {
        'post':post,
        'related':related,
        'gallery':gallery,
         
        }
    return render(request, 'single.html',context)    



def get_productadd(request):
    
    ImageFormset = modelformset_factory(ImageGallery, fields=("image",), extra=4)
    form = ProductAddForm(request.POST, request.FILES)
    formset = ImageFormset(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.save()
            for i in formset:
                try:
                    photo = ImageGallery(post=post, image=i.cleaned_data['image'])
                    photo.save()
                except Exception as e:
                    break  
            return redirect('index')          
    else:
        form = ProductAddForm()
        formset = ImageFormset(queryset=ImageGallery.objects.none())

    context = {
        'form':form,
        'formset':formset
    }    
   
    return render(request, 'products/product_add.html', context)




def get_category_add(request):
    product_category_add = ProductCategoryAddForm(request.POST or None)
    if product_category_add.is_valid():
        product_category_add.save()
        return redirect('index')
    context ={
        'product_category_add':product_category_add
    }    
    return render(request, 'products/product_category_add.html', context)



def get_update(request, id):
    updateproduct = get_object_or_404(Product, id=id)
    form = ProductAddForm(request.POST or None, request.FILES or None, instance=updateproduct)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form':form
    }    

    return render(request, "products/product_update.html", context)



def get_delete(request, id):
    deleteproduct = get_object_or_404(Product, id=id)
    deleteproduct.delete()
    return redirect('index')
        


def get_product_datatable(request):
    product = Product.objects.all()
    context ={
        'product':product
    }
    return render(request, 'products/product_datatable.html', context)



#Add Cart
def get_add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
        )
    order_qs = Order.objects.filter(user=request.user, order_verify=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect('order_summary')
        else:            
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect('order_summary')    
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect('order_summary')


#Remove Cart
def get_remove_form_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        order_verify=False
    )

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")  
            return redirect('index')

        else:
            messages.info(request, "This item was not in your cart")
            return redirect('index')

    else:
        messages.info(request, "You do not have an active order")
        return redirect('index')


def get_order_summary(request):

    try:
        order = Order.objects.get(user=request.user, order_verify=False)
        context = {
            'object':order
            }
        return render(request, 'products/summary.html', context)
    except:
        messages.error(request, "You do not have activate order")
        return redirect('/')



def get_single_remove_form_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        order_verify=False
    )

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
            else:
                order.items.remove(order_item)  

            messages.info(request, "This quantity is updated")  
            return redirect('order_summary')

        else:
            messages.info(request, "This item was not in your cart")
            return redirect('order_summary')

    else:
        messages.info(request, "You do not have an active order")
        return redirect('order_summary')        



def get_orderitem(request, id):
    orderitem = get_object_or_404(OrderItem, id=id)
    print(orderitem)
    orderitem = OrderItemForm(request.POST or None, instance=orderitem)
    if orderitem.is_valid():
        orderitem.save()
        return redirect('index')
    context = {
        'orderitem':orderitem,
        'orderitem':orderitem
       }    
    return render(request, "Order/orderitem.html", context)



def get_orderitem_delete(request, id):
    orderitem_delete = get_object_or_404(OrderItem, pk=id)
    print(orderitem_delete)
    orderitem_delete.delete()
    return redirect('index')    


def get_subcategory(request):
    form = SubcategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
       'form':form
    }    
    return render(request, 'products/subcategory.html', context)    


def get_checkout(request):
    form = CheckOutForm(request.POST or None)
    try:
        order=Order.objects.get(user=request.user, order_verify=False)
        if form.is_valid():
            mobile_number = form.cleaned_data.get('mobile_number')
            billing_address = BillingAddress(
                user = request.user,
                mobile_number = mobile_number,   
                )
            billing_address.save()
            order.billing_address = billing_address
            order.save()
            return redirect(reverse('payment', kwargs={'id': order.id}))
    except:
        return redirect('index')         
    context = {
        'form':form,
        'order':order,
         
    } 
    return render(request, 'products/checkout.html', context)        