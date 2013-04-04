from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^memed/$','appy.views.home',name='pccr_home'),
	url(r'^memed/login/$','appy.views.login_user',name='memed_user_login'),
	url(r'^memed/logout/$','appy.views.logout_user',name='memed_user_logout'),
	url(r'^memed/registerme/$','appy.views.registerme',name='memed_user_register'),
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
