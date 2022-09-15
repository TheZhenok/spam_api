from . import get_env_variable
from art import tprint

SECRET_KEY = get_env_variable("SECRET")
TEST = get_env_variable("TEST")

# ----------------------------------------------

DEBUG = True
ROOT_URLCONF = 'settings.urls'
WSGI_APPLICATION = 'settings.wsgi.application'

# ----------------------------------------------

EMAIL_USE_TLS = True
EMAIL_HOST = get_env_variable("EMAIL_HOST")
EMAIL_HOST_USER = get_env_variable("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_PASSWORD")
EMAIL_PORT = get_env_variable("EMAIL_PORT")

#  ---------------------------------------------

REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'

# ----------------------------------------------

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'




tprint(TEST)