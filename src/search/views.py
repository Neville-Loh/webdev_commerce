from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
	template_name = "search/view.html"

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProductView, self).get_context_data(*args, **kwargs)
		context['query'] = self.request.GET.get('q')

		if self.request.GET.get('box') == "true":
			self.template_name = "search/viewbox.html"
		# SeachQuery.objects.create(query=query)
		return context

	def get_queryset(self, *args, **kwargs):
		'''
		__icontains = field contains it
		__iexact = field exactly equal this
		'''
		request = self.request
		query = request.GET.get('q')
		if query is not None:
			return Product.objects.search(query)      # distance prevent rendering same product twice
		return Product.objects.none()
