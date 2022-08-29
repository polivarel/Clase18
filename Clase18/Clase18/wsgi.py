"""
WSGI config for Clase18 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os,django

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Clase18.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Clase18.settings'
settings.configure(default_settings=Clase18, DEBUG=True)
django.setup()
#from django.core.management import call_command


application = get_wsgi_application()
