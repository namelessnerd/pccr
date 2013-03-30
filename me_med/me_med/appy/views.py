# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def home(request):
	return render_to_response('forum_home.html')

def register(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('forum_register.html',c)

def registerme(request):
	
	name= request.POST
	user = User.objects.create_user(request.POST['name'], request.POST['email'],
			request.POST['password'])
	user.save()
	return render_to_response('forum_register_confirm.html')
