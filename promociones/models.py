from django.db import models

class Promociones(models.Models):
	restorant= models.CharField(max_length=100)
	promotion= models.CharField(max_length=200)
	restrictions= models.CharField(max_length=150)

def __str__(self):
	return"%s %s %s" % (
		self.restaurant
		self.promotion
		self.restrictions
		self.)
