from django.db import models
from django.contrib.auth.models import User

class Users(model.Model):
	name = models.CharFierld(max_length=100)
	last_name = models.CharFierld(max_length=100)
	email = models.CharFierld(max_length=100)
	password = models.CharFierld(max_length=100)
	password_confirmation = models.CharFierld(max_length=100)
