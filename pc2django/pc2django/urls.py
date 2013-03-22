from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$','pccrportal.views.home',name='pccr_home'),
	url(r'^about$','pccrportal.views.about',name='pccr_about'),
    url(r'^register/', 'pccrportal.views.register_researcher',name='register_researcher'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

    # url(r'^researcher/participant/register$','pccrportal.views.register_researcher',name='pccr_home'),
    # url(r'^$', 'pc2django.views.home', name='home'),
    # url(r'^$', 'pc2django.views.home', name='home'),
    # url(r'^pc2django/', include('pc2django.foo.urls')),
