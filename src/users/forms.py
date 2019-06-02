from django import forms
from django.contrib.auth.models import User  # Usermodel 
from django.contrib.auth.forms import UserCreationForm # User creation form

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		# keeping config in one place
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class GuestForm(forms.Form):
	email 	= forms.EmailField()