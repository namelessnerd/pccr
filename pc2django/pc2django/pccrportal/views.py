# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from pccrportal.models import Project


def foo(request):
	return render_to_response('pccrportal/foo.html')

def home(request):
	template_dict= {
			'title':'Patient Centric Collaborative Research','link_class_home':'active',
			'show_nav':0,
			}
	template_dict.update(csrf(request))
	return render_to_response('pccrportal/index.html',template_dict)

def register_researcher(request):
	if request.POST['code']=='acn techlabs dh 2013':
		try:
			user = User.objects.create_user(username= request.POST['email'],password= request.POST['password'])
			print request.POST['password']
			user.save()
		except Exception:
			c = {'title':'Welcome to PCCR','login_error':True, 'message':'Email you entered is not unique',}
			c.update(csrf(request))
			return render_to_response('pccrportal/index.html',c)

		user= authenticate(username= request.POST['email'],password= request.POST['password'])
		login(request, user)
		#return redirect('/pccr/user')
		return HttpResponse('Hello world')
	else:
		c = {'title':'Welcome to Me-Med','login_error':True, 'message':'The code you entered is wrong',}
		c.update(csrf(request))
		return render_to_response('pccrportal/index.html',c)


def login_register_user(request):
		if request.POST['action']=='login':
				return login_user(request)
		elif request.POST['action']=='register':
				return register_researcher(request)
		else:
				c = {'title':'Patient Centric Collaborative Care','login_error':True,
								'message':'The action you are doing is not supported',}
				c.update(csrf(request))
				return render_to_response('pccrportal/index.html',c)

def login_user(request):
		print request
		username= request.POST['email']
		password= request.POST['password']
		user= authenticate(username= username, password= password)
		if user is not None:
				if user.is_active:
						login(request, user)
						return redirect('/pccr/researcher')
				else:
						c = {'title':'Welcome to Me-Med','login_error':True, 'message':'Your account is no longer active. Register again.', }
						c.update(csrf(request))
						return render_to_response('forum_home.html',c)
		else:
				c = {'title':'Welcome to Me-Med','login_error':True, 'message':'An account with the email does not exist.',}
				c.update(csrf(request))
				return render_to_response('forum_home.html',c)

@login_required
def researcher_home(request):
	user_projects= Project.objects.filter(posted_by=request.user)
	template_dict= {
			'title':'PCCR Researcher Home','link_class_home':'active',
			'show_nav':1,
			'user_signed':True,
			'userid':request.user.username,
			'project_list': user_projects,
			}
	template_dict.update(csrf(request))
	print user_projects
	return render_to_response('pccrportal/researcher_home.html',template_dict)

@login_required
def add_project(request):
		print request
		current_project= Project(project_title=request.POST['project-title'],
						project_url=request.POST['pcori-url'],
						project_description= request.POST['project-description'],
						posted_by= request.user)
		current_project.save()
		return redirect('/pccr/researcher')


def about(request):
	return render_to_response('pccrportal/about.html',{'title':'About PCCR','link_class_about':'active',})

def project(request,pid):
	current_project= Project.objects.get(id= pid)
	print current_project.posted_by
	inputs = {'title':current_project.project_title,
					'description':current_project.project_description,
					'researchers':current_project.posted_by,
					'show_nav':1,
					}
	if request.user:
			inputs.update({'user_signed':True, 'userid':request.user.username,})
			if current_project.posted_by==request.user:
					inputs.update({'current_researcher_is_project_owner':True,})

	inputs.update(csrf(request))
	inputs['matches']=[{'name':name, 'topic':'Marzipan'} for  name in ['Brad Ruderman','Annie Chiang','Danny Daniels',]]
	return render_to_response('pccrportal/study.html',inputs,)

def user_modal(request):
	inputs = {}
	inputs['patient_name']='Sophia Cao'
	inputs['patient_sex']='F'
	inputs['patient_dob']='1/18/1991'
	inputs['reasons']=[{'reason':reason, 'detail':'detail'} for reason in ['Member of', 'Posts on', 'Has started posts on',]]
	return render_to_response('pccrportal/user_modal.html',inputs,)



#def register_participant(request):
	#return render_to_response('pccrportal/register.html')
	#return render_to_response('researcher/register.html')
