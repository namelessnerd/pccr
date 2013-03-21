# Create your views here.

from django.shortcuts import render_to_response

def home(request):
	return render_to_response('pccrportal/index.html',{'title':'Platform for Patient Centric Collaborative Care'})

def register_researcher(request):
	return render_to_response('pccrportal/register.html')
	#return render_to_response('researcher/register.html')

def register_participant(request):
	return render_to_response('participant/register.html')


