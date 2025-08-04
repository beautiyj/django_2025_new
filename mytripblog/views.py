from django.shortcuts import render

def index(request):
    return render(
	request,
	'mytripblog/index.html',
	)

