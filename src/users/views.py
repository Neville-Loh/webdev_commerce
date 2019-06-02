from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import GuestEmail
from .forms import UserRegisterForm, LoginForm, GuestForm

def register(request):
	# If get post request, initiate usercreatFrom with post data, else empty form
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# checking if data is valid
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created!')
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form":form
	}
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None

	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
			 	return redirect(redirect_path)
			else:
				return redirect("/")
	return render(request, "users/login.html", context)

def guest_register_view(request):
	form = GuestForm(request.POST or None)
	context = {
		"form":form
	}
	next_ = request.GET.get('next')
	next_post = request.POST.get('next')
	redirect_path = next_ or next_post or None

	if form.is_valid():
		email	 = form.cleaned_data.get("email")
		new_guest_email = GuestEmail.objects.create(email=email)
		request.session['guest_email_id'] = new_guest_email.id

		if is_safe_url(redirect_path, request.get_host()):
		 	return redirect(redirect_path)
		else:
			return redirect("/register/")
	return render("/register/")

@login_required
def profile(request):
	return render(request, 'users/profile.html')

# #self note
# type of the messages
# message.debug
# message.info
# message.success
# message.warning
# message.error