#Vaid E-comerce Project
A test project for Vaid interns


*ecomerce project ja kisu ache :
1.Login
Logout
SignUp
EmailConfirmation/Account Verify
Social auth
  Github , Linkedin, Google, Facebook
Category/subcategory
Single page
Category Related product
Total product list
Product add / Product Update/ Product delete
Multiple image
Add Card
Remove Card
Updated Card
Checkout
Payment system 
  Bkash/Rocket/Bank

<-----------------------------------------------Card Add Function------------------------------------------------->
Add Card er janno ja function ta korchi ....:
Function Name get_add_to_cart : ai function diya product Card add korano hoyache ..
first User ke product choice korta hoba ..shei janno request korba (request, slug)
item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
        )
choice korer por order_item create kora hoiche ...
order_qs = Order.objects.filter(user=request.user, order_verify=False)
akhon User check o order_verify check korer por shotto arop kore hoiche
if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect('order_summary')
 jodi product Card add theke abar jodi same product Card add kori tahole Quantity incress hoba..           
else:            
      order.items.add(order_item)
      messages.info(request, "This item was added to your cart.")
      return redirect('order_summary') 
r product na theke ba notun kon product add korla cart update hobe.


<----------------------------------Card Remove Function-------------------------------------->

Remove Card janno ja function ta korchi ....:
Function Name get_remove_form_cart : ai function prothom check korba Card Product ache ki na ...
order_qs = Order.objects.filter(
        user=request.user,
        order_verify=False
    )
jodi Card kon product theke tahole Card theke product remove hobe...
sha janno order_qs ta ke check korta hoba 
jodi order_qs exists hoi toba
if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart")  
            return redirect('index')

  tachara message show korba 
    
  else:
       messages.info(request, "This item was not in your cart")
       return redirect('index')
       
       
<--------------------------------------  Single product remove Card----------------------------->     
Function Name get_single_remove_form_cart: Card theke Product quantity decrease korer janno get_single_remove_form_cart
Function ta use kore hoyache....Romove Card Moto prothom check korba 
item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        order_verify=False
    )
jodi Card product theke toba or order_qs exists korba 
if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
jodi Card product poriman 1 theke besi hoi toba single kore romove hoba 
r jodi Card kon product na theke toba 
else:
   order.items.remove(order_item)
r potibar message framework maddhoma message show koraba..........


<--------------------------------- CheckOut Function------------------------------------------------------>
Function Name Checkout : a function Customer sokol poker address input deya deba...Input field gulu hoilo Mobile number etc.
check korba Card kon product ache ki na sha janno try and Exception use kore hoyache...


<----------------------------------------Payment Function---------------------------------------------------->
Function Name Payment: a function customer payment korba...prothoma ja order payment korba shei order ke request korba
(request,id) jodi request success hoi toba payment korba...payment field gula hossche--
user_order,
payment_method,
email,
mobile_number,
transaction,
time,
amount
payment model signals use kora hoyache......order model sathe payment model relation kora hoyache......jokhon sokol field thik thekba tokhon admin verify korba.jokhon payment model er payment_verify success hoba tokhon Order model er order_verify success hoba.......

