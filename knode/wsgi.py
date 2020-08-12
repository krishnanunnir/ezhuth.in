"""
WSGI config for knode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application
env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'.env')  
load_dotenv(env_file)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knode.settings')

application = get_wsgi_application()
