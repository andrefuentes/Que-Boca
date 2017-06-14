from django.db import models

# Create your models here.
class Avatares(models.Model) :
	Photo= models.ImageField()
	Character= models.CharField(max_length=100)
