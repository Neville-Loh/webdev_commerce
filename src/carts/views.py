from django.shortcuts import render
from .models import Cart

def cart_create(user=None)
	cart_obj = Cart.objects.create(user=None)
	pass


def cart_home(request):
	cart_id = request.session.get("cart_id", None)

	if cart_id is None and isinstance(cart_id, int):
		cart_obj = Cart.objects.create(user=None)
		request.session['cart_id'] = cart_obj.id
		print('New Cart Id created')

	else:
		print('cart ID exists')
		print(cart_id)
		cart_obj = Cart.objects.get(id=cart_id)
	#print( request.session)
	#print(dir(request.session))

	# request.session.session_key
	# request.session.set_expiry(300)  # 300 sec = 5 min

	#request.session['cart_id'] = 12   # setter dictionary ,
	 								#to get, request.session.get("cart_id", "Unknown"), if card id doesn't exist set as unknown

	return render(request,"carts/home.html",{})