from django.db import models
from django.urls import reverse
from datetime import datetime, date
# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=122)
	phone = models.CharField(max_length=12)
	comments = models.TextField()
	date = models.DateField()

	def __str__(self):
		return self.name

class Banner(models.Model):
	name = models.CharField(max_length=50)
	banner = models.ImageField(upload_to='banner/')

	def __str__(self):
		return self.name

	@staticmethod
	def get_banner():
		return Banner.objects.all()

class FirstBanner(models.Model):
	name = models.CharField(max_length=50)
	banner = models.ImageField(upload_to='banner/')

	def __str__(self):
		return self.name

	@staticmethod
	def get_fbanner():
		return FirstBanner.objects.all()

class Course(models.Model):
	"""docstring for Courses"""
	name=models.CharField(max_length=122)
	image=models.ImageField(upload_to='courses/')
	bigImage=models.ImageField(upload_to='courses/',default='')
	price=models.IntegerField(default=0)
	description=models.CharField(max_length=500, default='')
	Duration=models.CharField(max_length=200)
	time=models.CharField(max_length=122)
	module=models.CharField(max_length=1000, blank=True,default='')
	points=models.TextField(blank=True,default='')
	slug=models.SlugField(max_length=200, default='')

	class Meta:
		index_together = (('id', 'slug'),)
		
			

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('womenlab:course_detail', args=[self.id, self.slug])
	
	def get_url(self):
		return reverse('womenlab:pay_detail', args=[self.id, self.slug, self.price])

	def get_pay(self):
		return reverse('womenlab:pay', args=[self.id])
	@staticmethod
	def get_course():
		return Course.objects.all()


class Order(models.Model):
	course_name = models.CharField(max_length=122)
	name = models.CharField(max_length=122)
	email = models.EmailField(max_length = 254)
	date = models.DateField(default=datetime.now, blank=True)
	time = models.TimeField(default=datetime.now, blank=True)
	phone = models.CharField(max_length=12)
	amount= models.IntegerField(default=0)
	payment_id = models.CharField(max_length=100)
	paid = models.BooleanField(default=False)


	def __str__(self):
		return self.name

	






		


	
		



		

		