# Create your views here.

from django.shortcuts import render_to_response

def home(request):
	return render_to_response('pccrportal/index.html',{'title':'Platform for Patient Centric Collaborative Care','link_class_home':'active',})

def register_researcher(request):
	return render_to_response('researcher/register.html')

def about(request):
	return render_to_response('about.html',{'title':'About PCCR','link_class_about':'active',})

#def register_participant(request):
	#return render_to_response('pccrportal/register.html')
	#return render_to_response('researcher/register.html')