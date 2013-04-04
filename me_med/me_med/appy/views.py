# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
	c = {'title':'Welcome to Me-Med'}
	c.update(csrf(request))
	return render_to_response('forum_home.html',c)

def register(request):
	return render_to_response('forum_register.html',c)

def login_user(request):
		username= request.POST['email']
		password= request.POST['password']
		user= authenticate(username= username, password= password)
		if user is not None:
				if user.is_active:
						if login(request, user):
							return render_to_response('forum_register_confirm.html',{'user_signed':True,'userid':username, })
						else:
							return render_to_response('forum_register_confirm.html',{'user_signed':True,'userid':username, })
							'''
							c = {'title':'Welcome to Me-Med','login_error':True, 'message':'Check your username and password', }
							c.update(csrf(request))
							return render_to_response('forum_home.html',c)
							'''
				else:
						c = {'title':'Welcome to Me-Med','login_error':True, 'message':'Your account is no longer active. Register again.', }
						c.update(csrf(request))
						return render_to_response('forum_home.html',c)
		else:
				c = {'title':'Welcome to Me-Med','login_error':True, 'message':'An account with the email does not exist.',}
				c.update(csrf(request))
				return render_to_response('forum_home.html',c)



def logout_user(request):
		logout(request)
		return home(request)

def registerme(request):
	
	name= request.POST
	user = User.objects.create_user(username= request.POST['email'],password= request.POST['password'])
	print request.POST['password']
	user.save()
	return render_to_response('forum_register_confirm.html',{'user_signed':True,'userid':request.POST['email'],})

def forum_explore(request):
		return render_to_response('forum_view.html')
