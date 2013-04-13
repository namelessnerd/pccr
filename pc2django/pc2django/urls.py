from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^pccr$','pccrportal.views.home',name='pccr_home'),
	url(r'^pccr/login$','pccrportal.views.login_register_user',name='pccr_home'),
  url(r'^pccr/register/', 'pccrportal.views.login_register_user',name='register_researcher'),
	url(r'^pccr/logout$','pccrportal.views.home',name='pccr_home'),
	url(r'^pccr/researcher$','pccrportal.views.researcher_home',name='pccr_home'),
	url(r'^pccr/add_project$','pccrportal.views.add_project',name='pccr_home'),
	url(r'^pccr/about$','pccrportal.views.about',name='pccr_about'),
  url(r'^pccr/project/(\d+)','pccrportal.views.project',name='pccr_study'),
  url(r'^user','pccrportal.views.user_modal',name='pccr_user_modal'),  
  url(r'^foo','pccrportal.views.foo',name='pccr_foo'),  

    # Uncomment the admin/doc line below to enable admin documentation:
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

    # url(r'^researcher/participant/register$','pccrportal.views.register_researcher',name='pccr_home'),
    # url(r'^$', 'pc2django.views.home', name='home'),
    # url(r'^$', 'pc2django.views.home', name='home'),
    # url(r'^pc2django/', include('pc2django.foo.urls')),
