from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from web_project.utils import unique_slug_generator
from products.models import Product


'''
how to use many to many field of Tags:
When we do
from tags.models import Tag
Tag.object.all() will show all object,
Tag.object.first().products                   <<<< this willl call upon the default product manager, E.g.
Tag.object.first().products.all().first().title

However if we import product instead,
form products.models import Product
qs = product.objects.all()
prod = qs.first()
prod.tag will gives us error ** 

>> prod.tag_set <<< is the right command.

'''

class Tag(models.Model):
	title 		= models.CharField(max_length=120)
	slug   		= models.SlugField()
	timestamp	= models.DateTimeField(auto_now_add=True)
	active		= models.BooleanField(default=True)
	products 	= models.ManyToManyField(Product, blank=True)

	def __str__(self):
		return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwagrs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Tag)