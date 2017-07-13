from django.shortcuts import render
from Promociones.models import promociones

def Promociones(request):
	promociones=Promociones.object.all(),
	promociones_tar=promocionesForm(),
	return render(request,'pagina principal',{'promociones':promociones},
		)

