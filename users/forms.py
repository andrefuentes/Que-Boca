from django import forms
from users.models import Users

class UsersForm(forms.ModelsForm):
	class Meta:
		models=Users
		fields=[
		'name',
		'last name',
		'email',
		'password',
		'password confirmation'
		]
		