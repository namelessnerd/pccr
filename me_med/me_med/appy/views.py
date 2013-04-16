# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import simplejson

from appy.models import Conversation


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
						login(request, user)
						return redirect('/memed/user')
				else:
						c = {'title':'Welcome to Me-Med','login_error':True, 'message':'Your account is no longer active. Register again.', }
						c.update(csrf(request))
						return render_to_response('forum_home.html',c)
		else:
				c = {'title':'Welcome to Me-Med','login_error':True, 'message':'An account with the email does not exist.',}
				c.update(csrf(request))
				return render_to_response('forum_home.html',c)

def logout_user(request):
		print request.user
		logout(request)
		print request.user
		return home(request)

def registerme(request):
	if request.POST['code']=='acn techlabs dh 2013':
		try:
			user = User.objects.create_user(username= request.POST['email'],password= request.POST['password'])
			print request.POST['password']
			user.save()
		except Exception:
			c = {'title':'Welcome to Me-Med','login_error':True, 'message':'Email you entered is not unique',}
			c.update(csrf(request))
			return render_to_response('forum_home.html',c)

		user= authenticate(username= request.POST['email'],password= request.POST['password'])
		login(request, user)
		return redirect('/memed/user')
	else:
		c = {'title':'Welcome to Me-Med','login_error':True, 'message':'The code you entered is wrong',}
		c.update(csrf(request))
		return render_to_response('forum_home.html',c)


@login_required
def show_profile(request):
	return render_to_response('user_profile.html',{'user_signed':True,'userid':request.user.username,})


def forum_explore(request):
		return render_to_response('forum_view.html')

@login_required
def add_conversation(request):
		conversation= Conversation(conversation_title=request.POST['conversation_title'],conversation_message=
						request.POST['conversation_message'].strip(), posted_by= request.user)
		try:
			conversation.save()
			return HttpResponse(simplejson.dumps({'status':1,'title':request.POST['conversation_title'],'id':conversation.id,}))
		except Exception, e:
			return HttpResponse(simplejson.dumps({'status':0,}))


# a hack to get all users. need a better approach later

def show_posts(request, uid):
	conversations= Conversation.objects.get(posted_by=uid)
	return render_to_response('user_posts.html', {'posts':conversations})




