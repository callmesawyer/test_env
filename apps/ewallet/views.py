from django.shortcuts import render


from django.http import HttpResponse


def home(request):
	context = {
		'title' : 'Home Page',
		'name' : 'Roshan Maharjan' 
	}
	return render(request, 'home.html', context)

def contact(request):
	return HttpResponse('Contact us at: 01:4333234')