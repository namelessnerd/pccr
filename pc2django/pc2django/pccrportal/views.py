# Create your views here.

from django.shortcuts import render_to_response

def foo(request):
	return render_to_response('pccrportal/foo.html')

def home(request):
	return render_to_response('pccrportal/index.html',{'title':'Platform for Patient Centric Collaborative Care','link_class_home':'active',})

def register_researcher(request):
	return render_to_response('researcher/register.html')

def about(request):
	return render_to_response('pccrportal/about.html',{'title':'About PCCR','link_class_about':'active',})

def study(request):
	inputs = {}
	inputs['title']='Project Name'
	inputs['researchers']='Researcher A. Name & Researcher B. Name'
	inputs['description']='Turn-key, "methodologies wikis citizen-media B2C dot-com networks reinvent deliverables, best-of-breed e-markets evolve back-end, scale frictionless." Content; deliverables monetize integrateAJAX-enabled relationships unleash mindshare reinvent wireless, extensible eyeballs. Engineer mesh; user-contributed granular target interactive deploy streamline unleash: compelling action-items rich-clientAPIs grow matrix, revolutionize web-readiness. Syndicate sticky blogging deliverables engineer transparent web services, user-centred reinvent addelivery applications synergies.'
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
