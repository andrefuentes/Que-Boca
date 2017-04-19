from django.db import models

class Promociones(models.Models):
	place= models.CharField(max_length=100)
	promotion= models.CharField(max_length=200)
	restrictions= models.CharField(max_length=150)

