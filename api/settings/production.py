import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'p6h2t2+i+2fh)8yfu%_d_#p17lopc@iwa4d*-rln^fi#p1*h_b'

BASE_URL = 'http://website-name.com/'

DEBUG = False

ALLOWED_HOSTS = []



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DROPBOX_OAUTH2_TOKEN = os.environ.get('DROPBOX_OAUTH2_TOKEN')
# DROPBOX_ROOT_PATH = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
