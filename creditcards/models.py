from django.db import models

# Create your models here.
class CreditCard(models.Models) :
	name= models.CharField(max_length=100)
	bank= models.CharField(max_length=100)
	brand= models.CharField(max_length=100)