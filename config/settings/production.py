from .base import *


DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xxx',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx.xxx.xxx',
        'PORT': '5432',
    }
}
