from django import forms
from promociones.models import promociones

class PromForms(forms.ModelsForm) :
	class Meta:
		models=promociones 
		fields[
		'restaurant',
		'creditcard',
		'typeoffood',
		]