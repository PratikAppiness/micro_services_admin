from django.db import models

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=200, verbose_name='Title')
  image = models.CharField(max_length=200,verbose_name='Image Path')
  likes = models.PositiveBigIntegerField(default=0,verbose_name='Likes')

class User(models.Model):
  pass