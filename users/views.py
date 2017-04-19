from django.shortcuts import render
from users.models import Users
from users.form import UserForm
from django.contrib.auth.models import  login

def create_user (request):
	users= Users.objects
