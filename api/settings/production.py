import os
import django_heroku
from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.environ.get('SECRET_KEY')

BASE_URL = os.environ.get('BASE_URL')

DEBUG = False

ALLOWED_HOSTS = ['findyourapi.herokuapp.com',
                 'www.findyourapi.herokuapp.com',
                 'masterbdx.findyourapi.herokuapp.com',
                 'findyourapi.com',
                 'www.findyourapi.com',
                 'masterbdx.findyourapi.com']

MAIN_EMAIL = os.environ.get('MAIN_EMAIL')
ADMINS = [('masterbdx', MAIN_EMAIL)]


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = os.environ.get('DROPBOX_OAUTH2_TOKEN')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# SendGrid Email Host
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# # Defender Settings

DEFENDER_REDIS_URL = os.environ.get('REDIS_URL')

django_heroku.settings(locals())