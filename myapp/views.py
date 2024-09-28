from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, JsonResponse
from .models import Cart, Category, Food, profile, OrderDetail,Delivery_boy_profile,Delivery_order
from django.db.models import Q, F, Sum, ExpressionWrapper, FloatField

# from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    context = {}
    # fetch data from html form
    if request.method == 'POST':
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = User.objects.filter(username=email)
        if len(check) == 0:
            # Save data to both tables
            myuser = User.objects.create_user(email, email, password)
            myuser.first_name = name
            myuser.save()

            Profile = profile(user=myuser, mobile=mobile)
            Profile.save()
            context['status'] = f'{name} Registered Successfully'
            # return redirect('login')
        else:
            context['error'] = f'{email} Already exists'

    return render(request, "register.html", context)


# @login_required(login_url="/login/")
def log(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('password')
        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff :
                return HttpResponseRedirect('/admin')
            request.session['email'] = email
            return HttpResponseRedirect('/home')
        else:
            context['error'] = 'Invalid Login Details'
    return render(request, "login.html", context)


def home(request):
    print(request.session.get('email'))
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def booking(request):
    return render(request, "booking.html")


def delivery_boy_signup(request):
    context = {}
    # fetch data from html form
    if request.method == 'POST':
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = User.objects.filter(username=email)
        if len(check) == 0:
            # Save data to both tables
            myuser = User.objects.create_user(email, email, password)
            myuser.first_name = name
            myuser.save()

            Delivery_boy_Profile = Delivery_boy_profile(
                user=myuser, mobile=mobile)
            Delivery_boy_Profile.save()
            context['status'] = f'{name} Registered Successfully'
            # return redirect('login')
        else:
            context['error'] = f'{email} Already exists'

    return render(request, "deliverysignup.html", context)


def delivery_boy_login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('password')
        check_user = authenticate(username=email, password=passw)
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin')
            request.session['email'] = email
            return HttpResponseRedirect('/delivery_home_page')
        else:
            context['error'] = 'Invalid Login Details'
    return render(request, "deliverylogin.html", context)


def delivery_home_page(request):
    return render(request, "deliveryboy.html")



def lout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def food(request):
    food = None  # Food.get_all_Food()
    totaltitem = 0
    if request.session.has_key('email'):
        email = request.session['email']
        category = Category.get_all_category()
        totaltitem = len(Cart.objects.filter(email=email))
        cid = request.GET.get('category')
        if cid:
            food = Food.get_all_Food_by_category_id(cid)
        else:
            food = Food.get_all_Food()
        data = {
            'food': food,
            'category': category,
            'totaltitem': totaltitem
        }
        return render(request, "food.html", data)
    else:
        return redirect('login')


def foodetail(request, pk):
    totaltitem = 0
    food = Food.objects.get(pk=pk)
    email = request.session['email']
    totaltitem = len(profile.objects.filter(email=email))
    item_already_in_cart = False
    if request.session.has_key('email'):
        item_already_in_cart = Cart.objects.filter(
            Q(food=food.id) & Q(email=email)).exists()

        Data = {
            'food': food,
            'item_already_in_cart': item_already_in_cart,
            'totaltitem': totaltitem
        }
    return render(request, "foodetail.html", Data)


def add_to_cart(request):
    email = request.session['email']
    food_id = request.GET.get('food_id')
    food_name = Food.objects.get(id=food_id)
    food = Food.objects.filter(id=food_id)
    for f in food:
        image = f.image
        price = f.price
        Cart(email=email, food=food_name, image=image, price=price).save()
    return redirect(f"/foodetail/{food_id}")


# def show_cart(request):
#     totalitem = 0
#     subtotal = 0
#     if request.session.has_key('email'):
#         email = request.session['email']
#         totalitem = len(Cart.objects.filter(email=email))
#         customer = Cart.objects.filter(email=email)
#         for c in customer:
#             email = c.email
#             cart = Cart.objects.filter(email=email)
#             data = {
#                 'totalitem': totalitem,
#                 'cart': cart,
#                 'total': subtotal,
#                 'subtotal': subtotal,
#             }
#             if cart:
#                 return render(request, "show_cart.html", data)
#             else:
#                 return render(request, "empty_cart.html")
#     return render(request, "empty_cart.html")

def show_cart(request):
    if request.session.has_key('email'):
        email = request.session['email']
        cart_items = Cart.objects.filter(email=email)

        if cart_items:
            total_amount = Cart.objects.filter(email=email).annotate(
                amount = ExpressionWrapper( F('quantity') * F('price'), output_field=FloatField())            
            ).aggregate(total_amount = Sum(F('amount')))['total_amount']
            data = {
                'totalitem': len(cart_items),
                'cart_items': cart_items,
                'total': total_amount,
                'subtotal': total_amount,
            }
            return render(request, "show_cart.html", data)
        else:
            return render(request, "empty_cart.html")
    return render(request, "empty_cart.html")

# def plus_cart(request):
#     if request.session.has_key('email'):
#         email = request.session["email"]
#         prod_id = request.GET['prod_id']
#         customer = User.objects.filter(email=email)
#         for us in customer:
#             c1 = Cart.objects.get(Q(food=prod_id) & Q(email=email))
#             c1.quantity += 1
#             c1.save()
#         subtotal = 0.0
#         cart = Cart.objects.filter(email=email)
#         for c in cart:
#             user = c.email
#             cart_prods = [p for p in Cart.objects.all() if p.email == user]
#             if cart_prods:
#                 for p in cart_prods:
#                     tempTotal = p.quantity * \
#                         Food.objects.filter(id=prod_id)[0].price
#                     subtotal += tempTotal
#                 data = {
#                     'quantity': c1.quantity,
#                     'subtotal': subtotal,
#                     'total': subtotal,
#                 }
#                 return JsonResponse(data)
#     else:
#         return redirect('login')

def plus_cart(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        prod_id = request.GET['prod_id']

        cart_item = Cart.objects.get(food=prod_id ,email=email)
        cart_item.quantity += 1
        cart_item.save()

        subtotal = Cart.objects.filter(email=email).annotate(
            amount = ExpressionWrapper( F('quantity') * F('price'), output_field=FloatField())            
        ).aggregate(total_amount = Sum(F('amount')))['total_amount']

        data = {
            'quantity': cart_item.quantity,
            'subtotal': subtotal,
            'total': subtotal,
        }
        print('➡ myapp/views.py:241 data:', data)
        return JsonResponse(data)
    return redirect('login')


# def minus_cart(request):
#     if request.session.has_key('email'):
#         email = request.session["email"]
#         prod_id = request.GET['prod_id']
#         customer = User.objects.filter(email=email)
#         for us in customer:
#             c1 = Cart.objects.get(Q(food=prod_id) & Q(email=email))
#             c1.quantity -= 1
#             c1.save()
#         subtotal = 0.0
#         cart = Cart.objects.filter(email=email)
#         for c in cart:
#             user = c.email
#             cart_prods = [p for p in Cart.objects.all() if p.email == user]
#             if cart_prods:
#                 for p in cart_prods:
#                     tempTotal = p.quantity * \
#                         Food.objects.filter(id=prod_id)[0].price
#                     subtotal += tempTotal
#                 data = {
#                     'quantity': c1.quantity,
#                     'subtotal': subtotal,
#                     'total': subtotal,
#                 }
#                 return JsonResponse(data)
#     else:
#         return redirect('login')


def minus_cart(request):
    if request.session.has_key('email'):
        email = request.session["email"]
        prod_id = request.GET['prod_id']

        cart_item = Cart.objects.get(food=prod_id ,email=email)
        cart_item.quantity -= 1
        cart_item.save()

        quantity = cart_item.quantity

        if cart_item.quantity <= 0: 
            cart_item.delete()

        subtotal = Cart.objects.filter(email=email).annotate(
            amount = ExpressionWrapper( F('quantity') * F('price'), output_field=FloatField())            
        ).aggregate(total_amount = Sum(F('amount')))['total_amount']

        data = {
            'quantity': quantity,
            'subtotal': subtotal,
            'total': subtotal,
        }
        print('➡ myapp/views.py:241 data:', data)
        return JsonResponse(data)
    return redirect('login')


def remove_cart(request):
    if request.session.has_key('email'):
        cart_id = request.GET.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        return redirect('show_cart')
    else:
        return redirect('login')


def checkout(request):

    totalitem = 0

    if request.session.has_key('email'):
        email = request.session["email"]
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        # print(name,email,mobile,address)
        cart_food = Cart.objects.filter(email=email)
        for c in cart_food:
            qty = c.quantity
            price = c.price
            food_name = c.food
            image = c.image

            OrderDetail(user=email, food_name=food_name,image=image, qty=qty, price=price,address=address).save()
            cart_food.delete()

            totalitem = len(Cart.objects.filter(email=email))
            customer = User.objects.filter(email=email)
            for c in customer:
                email = c.email

            data = {

                'email': email,
                'totalitem': totalitem
            }

            return render(request, 'empty_cart.html', data)
    else:
        return redirect('login')


def order(request):
    totalitem = 0
    if request.session.has_key('email'):
        email = request.session["email"]
        totalitem = len(Cart.objects.filter(email=email))
        customer = User.objects.filter(email=email)
        for c in customer:
            name = c.email
            order = OrderDetail.objects.filter(user=email)
            data = {
                'order': order,
                'name': name,
                'totalitem': totalitem,
            }
            if order:
                return render(request, 'order.html', data)
            else:
                return render(request, 'empty_order.html')
    else:
       return render(request, 'empty_order.html')


def delivery_home_page(request):
    totalitem = 0
    if request.session.has_key('email'):
        email = request.session["email"]
        totalitem = len(Cart.objects.filter(email=email))
        customer = User.objects.filter(email=email)
        for c in customer:
            name = c.email
            order = OrderDetail.objects.filter(user=email)
            data = {
                'order': order,
                'name': name,
                'totalitem': totalitem,
            }
            if order:
                return render(request, 'deliveryboy.html', data)
            else:
                return render(request, 'deliveryboy.html')
    else:
        return redirect('delivery_boy_login')
    

def delete_order(request,id):
    order_delete=OrderDetail.objects.get(id=id)
    order_delete.delete()
    return redirect('/order')
