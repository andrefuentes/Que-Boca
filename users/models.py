from django.db import models
from django.contrib.auth.models import User

class Users(model.Model): 
	username = models.CharFierld(max_length=100)
	email = models.CharFierld(max_length=100)
	password = models.CharFierld(max_length=100)
