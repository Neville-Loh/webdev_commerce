"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
########### Static local config ####################################
from django.conf import settings
from django.conf.urls.static import static
####################################################################

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include

# User view
from users import views as user_views 
# Product View
from products.views import (
    ProductListView, 
    ProductDetailView,
    ProductDetailSlugView, 
    ProductFeaturedListView,
    ProductFeaturedDetailView,

    # function based view testing
    # product_list_view,
    # product_detail_view, 
    )

# cart view
from carts.views import cart_home

# default django login logout view'ProductFeaturedtListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), 

    # User url
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # as_view set the directory of html
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # Product url
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^cart/$',cart_home, name='cart'),

]

####### If DEBUG is On, turn on local static ################################
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#####################################################################################