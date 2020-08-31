from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title


	def get_absolute_url(self):

		return reverse('page-detail' , args=[self.id])
