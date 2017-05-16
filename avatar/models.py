from django.db import models

# Create your models here.
class Avatares(models.Model) :
	Photo= models.imagefield
	Character= models.CharField(max_length=100)
