__author__ = 'trippshealy'
from .settings import *

DATABASES = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'atusapi',
        'USER': 'tripp',
        'PASSWORD': '',
        'HOST': ''
    }
}