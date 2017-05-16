from django.db import models

# Create your models here.
class Configuracion(models.Model) :
	problem= models.CharField(max_length=100)
	questions= models.CharField(max_length=100)
	privacy=models.CharField(max_length=100)
	location= models.CharField(max_length=100)
	accounts= models.CharField(max_length=100)
	