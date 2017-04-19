from django.shortcuts import render
from CreditCard.models import creditcard

# Create your views here.
def lista_creditcards(request):
	creditcard