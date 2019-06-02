from django.shortcuts import render, redirect

from users.forms import LoginForm, GuestForm
from users.models import GuestEmail
from billing.models import BillingProfile
from orders.models import Order
from products.models import Product
from .models import Cart

def cart_create(user=None):
	cart_obj = Cart.objects.cart_create

def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request,"carts/home.html",{"cart": cart_obj})

def cart_update(request):
	print('Dis your request POST', request.POST)
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show messeage to user, products have been deleted")
			return redirect("cart:home")

		cart_obj, new_obj = Cart.objects.new_or_get(request)

		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items'] = cart_obj.products.count()

	return redirect("cart:home")

def checkout_home(request):
	cart_obj, cart_created = Cart.objects.new_or_get(request)
	order_obj = None
	if cart_created or cart_obj.products.count() == 0:
		return redirect("cart:home")

	login_form = LoginForm()
	guest_form = GuestForm()
	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	# guest_email_id = request.session.get('guest_email_id')

	# if user.is_authenticated:
	# 	# logged in user checkout; remember payment detail
	# 	billing_profile, billing_profile_created =BillingProfile.objects.get_or_create(
	# 													user=user, email= user.email)
	# elif guest_email_id is not None:
	# 	# guest user checkout; auto reloads payment detail
	# 	guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
	# 	billing_profile, billing_guest_profile_created = billing_guest_profile_created =BillingProfile.objects.get_or_create(
	# 													email= guest_email_obj.email)
	# else:
	# 	print("something has gone horiblly wrong")
	# 	pass

	if billing_profile is not None:
		order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
		

	context = {
		"object": order_obj,
		"billing_profile" : billing_profile,
		"login_form": login_form,
		"guest_form": guest_form
	}

	return render(request, "carts/checkout.html", context)