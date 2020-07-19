from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
	first_name = models.CharField('First Name', max_length=50)
	last_name = models.CharField('Last Name', max_length=50)
	author_email = models.CharField('Email', max_length=100)
	active = models.BooleanField(default=True)
	comment_texr = models.TextField('Text of comment')
	pub_date = timezone.now()
	def __str__(self):
		return self.first_name +' '+ self.last_name