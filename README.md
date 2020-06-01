# Vaid E-comerce Project
A test project for Vaid interns


## ecomerce project ja kisu ache :
1. Login
2. Logout
4. SignUp
5. EmailConfirmation/Account Verify
6. Social auth Github - Linkedin - Google - Facebook
7. Category/subcategory
8. Single page
9. Category Related product
10. Total product list
11. Product add / Product Update/ Product delete
12. Multiple image
13. Add Card
14. Remove Card
15. Updated Card
16. Checkout
17. Payment system 
    Bkash/Rocket/Bank

<-----------------------------------------------Card Add Function-------------------------------------------------> <br/>
:+1: Add Card er janno ja function ta korchi ....:/
Function Name get_add_to_cart : ai function diya product Card add korano hoyache ..
first User ke product choice korta hoba ..shei janno request korba (request, slug)<br/>
item = get_object_or_404(Product, slug=slug)<br/>
    order_item, created = OrderItem.objects.get_or_create(<br/>
        item = item,<br/>
        user = request.user,<br/>
        ordered = False<br/>
        )<br/>
choice korer por order_item create kora hoiche ...<br/>
order_qs = Order.objects.filter(user=request.user, order_verify=False)<br/>
akhon User check o order_verify check korer por shotto arop kore hoiche<br/>
if order_qs.exists():<br/>
        order = order_qs[0]<br/>
        if order.items.filter(item__slug=item.slug).exists():<br/>
            order_item.quantity +=1<br/>
            order_item.save()<br/>
            messages.info(request, "This item quantity was updated.")<br/>
            return redirect('order_summary')<br/>
 jodi product Card add theke abar jodi same product Card add kori tahole Quantity incress hoba..<br/>           
else:<br/>            
      order.items.add(order_item)<br/>
      messages.info(request, "This item was added to your cart.")<br/>
      return redirect('order_summary')<br/> 
r product na theke ba notun kon product add korla cart update hobe.<br/>


<----------------------------------Card Remove Function--------------------------------------><br/>

:smile: Remove Card janno ja function ta korchi ....:<br/>
Function Name get_remove_form_cart : ai function prothom check korba Card Product ache ki na ...<br/>
order_qs = Order.objects.filter(<br/>
        user=request.user,<br/>
        order_verify=False<br/>
    )<br/>
jodi Card kon product theke tahole Card theke product remove hobe...<br/>
sha janno order_qs ta ke check korta hoba<br/> 
jodi order_qs exists hoi toba<br/>
if order.items.filter(item__slug=item.slug).exists():<br/>
            order_item = OrderItem.objects.filter(<br/>
                item=item,<br/>
                user = request.user,<br/>
                ordered = False<br/>
            )[0]<br/>
            order.items.remove(order_item)<br/>
            messages.info(request, "This item was removed from your cart")<br/>  
            return redirect('index')<br/>

  tachara message show korba<br/> 
    
  else:<br/>
       messages.info(request, "This item was not in your cart")<br/>
       return redirect('index')<br/>
       
       
<--------------------------------------  Single product remove Card-----------------------------><br/>     
Function Name get_single_remove_form_cart: Card theke Product quantity decrease korer janno get_single_remove_form_cart<br/>
Function ta use kore hoyache....Romove Card Moto prothom check korba<br/> 
item = get_object_or_404(Product, slug=slug)<br/>
    order_qs = Order.objects.filter(<br/>
        user=request.user,<br/>
        order_verify=False<br/>
    )<br/>
jodi Card product theke toba or order_qs exists korba<br/> 
if order.items.filter(item__slug=item.slug).exists():<br/>
            order_item = OrderItem.objects.filter(<br/>
                item=item,<br/>
                user = request.user,<br/>
                ordered = False<br/>
            )[0]<br/>
            if order_item.quantity > 1:<br/>
                order_item.quantity -=1<br/>
                order_item.save()<br/>
jodi Card product poriman 1 theke besi hoi toba single kore romove hoba<br/> 
r jodi Card kon product na theke toba<br/> 
else:<br/>
   order.items.remove(order_item)<br/>
r potibar message framework maddhoma message show koraba..........<br/>


<--------------------------------- CheckOut Function------------------------------------------------------><br/>
Function Name Checkout : a function Customer sokol poker address input deya deba...Input field gulu hoilo Mobile number etc.<br/>
check korba Card kon product ache ki na sha janno try and Exception use kore hoyache...<br/>


<----------------------------------------Payment Function----------------------------------------------------><br/>
Function Name Payment: a function customer payment korba...prothoma ja order payment korba shei order ke request korba<br/>
(request,id) jodi request success hoi toba payment korba...payment field gula hossche--<br/>
user_order,<br/>
payment_method,<br/>
email,<br/>
mobile_number,<br/>
transaction,<br/>
time,<br/>
amount<br/>
payment model signals use kora hoyache......order model sathe payment model relation kora hoyache......jokhon sokol field<br/> thik thekba tokhon admin verify korba.jokhon payment model er payment_verify success hoba tokhon Order model er order_verify success hoba.......<br/>

