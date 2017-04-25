from django import forms
from users.models import Users

class UsersForm(forms.ModelsForm):
	class Meta:
		models=Users
		fields=[
		'user',
		'telefono',
		'ubicacion',
		]
		