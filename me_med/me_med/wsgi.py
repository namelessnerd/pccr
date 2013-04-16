SITE_DIR='/home/karthik/pccr-env/pccr/me_med/me_med'

import site

site.addsitedir(SITE_DIR)

import os
import sys
sys.path.append(SITE_DIR)
sys.path.append('/home/karthik/pccr-env/pccr/me_med/')

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

