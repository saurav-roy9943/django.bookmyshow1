import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmyshow.settings")

from bookmyshow.wsgi import application

def handler(environ, start_response):
    return application(environ, start_response)
