"""
WSGI config for httpapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
from os.path import dirname, abspath
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)))  # 3
sys.path.insert(0, PROJECT_DIR)  # 5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "httpapi.settings")

application = get_wsgi_application()
