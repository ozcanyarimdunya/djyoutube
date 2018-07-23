from .base import *

INSTALLED_APPS += [
    'videos.apps.VideosConfig',
]
ALLOWED_HOSTS = ['*']

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "djyoutube/assets/media")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "djyoutube/assets/static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "djyoutube/assets/static-dev"),
]
