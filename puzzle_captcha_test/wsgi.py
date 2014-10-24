"""
WSGI config for puzzlecaptcha.ransomsoft.com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_DIR)
sys.path.append(os.path.join(PROJECT_DIR, 'puzzle_captcha_test'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "puzzle_captcha_test.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
