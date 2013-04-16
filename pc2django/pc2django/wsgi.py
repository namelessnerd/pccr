import site

site.addsitedir(SITE_DIR)

import os
import sys
sys.path.append(SITE_DIR)
sys.path.append('/home/karthik/pccr-env/pccr/pc2django/')

os.environ['DJANGO_SETTINGS_MODULE']='settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
