from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product

# 2 type of views, object and funtion based
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}

	return render(request, "products/list.html", context)




class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context
	

def product_detail_view(request, pk=None, *args, **kwargs):
	#instance = Product.object.get(pk=pk) #id object created
	#instance = get_object_or_404(Product, pk=pk)
	# try:
	# 	instance = Product.objects.get(id=pk)
	# 	print('its doing something')
	# except Product.DoesNotExist:
	# 	print('no product')
	# 	raise Http404("product does not exist")
	# except:
	# 	print('something went really wrong')
	instance = Product.objects.get_by_id(pk)
	
	print(instance)
	qs = Product.objects.filter(id=pk)

	if qs.exists() and qs.count() == 1:
		instance = qs.first()
	else:
		raise Http404("product does not exist")
	context = {
		'object': instance
	}

	return render(request, "products/detail.html", context)