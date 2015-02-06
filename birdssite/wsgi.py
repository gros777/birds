"""
WSGI config for birdssite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

# original content
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "birdssite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# to deploy on PythonAniwere
# add your project directory to the sys.path
# project_home = u'/home/gros777/birds'
# if project_home not in sys.path:
#     sys.path.append(project_home)

# # set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE'] = 'birdssite.settings'

# # serve django via WSGI
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()

