import random
import string
import os
from django.db import models

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext

# changing file name to a random interger and pathing it
def upload_image_path(instance, filename):
	# print(instance)
	# print(filename)
	char_available = string.ascii_letters + '1234567890'
	new_filename = ''.join(random.choice(char_available) for i in range(2,random.randint(0,20)))
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
			new_filename=new_filename, 
			final_filename=final_filename
			)

class ProductManager(models.Manager):
	def get_by_id(self, id):
		# product.objects 
		return self.get_queryset().filter(id=id)


class Product(models.Model):
	title 		= models.CharField(max_length=120, blank=False)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=10000)
	feature 	= models.BooleanField(default=False) # null=True, default=True
	image		= models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	objects = ProductManager()


	def __str__(self):
		return self.title