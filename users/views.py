from django.shortcuts import render
from users.models import Perfil
from users.forms import UsersForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

def create_user(request):
	user = users.object.create_user(name,password,email,user)
	user.set_password('new password')
	user.save()
def login_user(request):
	username= request.POST['username']
	password= request.POST['password']
	user=authenticate(request,username=username,
		password=password)
	if user is not None:
		login(request,user)
	else:
		print("error")
		