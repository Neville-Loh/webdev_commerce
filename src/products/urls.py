from django.conf.urls import url 

from .views import (
    ProductListView, 
    #ProductDetailView,
    ProductDetailSlugView, 
    ProductFeaturedListView,
    ProductFeaturedDetailView,

    # function based view testing
    #product_list_view,
    #product_detail_view, 
    )

app_name = "products"
urlpatterns = [
    # Product url
    url(r'^$', ProductListView.as_view(), name='list'),
    #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

    # Funcntion based view for testing
    #url(r'^products-fbv/$', product_list_view),   
    #url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]