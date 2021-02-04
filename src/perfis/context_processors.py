

from .models import Perfil

def profile_pic(request):
	if request.user.is_authenticated:
		profile_obj = Perfil.objects.get(user=request.user)
		pic 		= profile_obj.avatar
		#returns a dictionary
		return {'picture': pic,}
	#has to return a empty dictionary to users not authenticated
	return {}