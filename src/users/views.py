from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm\

from django.contrib.auth.decorators import login_required

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