from django import forms
from users.models import Perfil

class UsersForm(forms.ModelForm):
	class Meta:
		models= Perfil
		fields=[
		'user',
		'telefono',
		'ubicacion',
		]
		