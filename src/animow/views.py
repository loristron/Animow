from django.shortcuts import render


def home_view(request, *args, **kwargs):
	context = {
		"page_title": "Animow",
	}
	return render(request, 'home.html', context)