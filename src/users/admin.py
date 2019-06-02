from django.contrib import admin
from .models import Profile, GuestEmail


admin.site.register(Profile)
admin.site.register(GuestEmail)