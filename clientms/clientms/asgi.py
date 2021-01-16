"""
ASGI config for CMS_Clients project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clientms.settings')

application = get_asgi_application()
