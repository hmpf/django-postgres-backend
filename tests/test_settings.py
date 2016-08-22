import os

import dj_database_url


SECRET_KEY = 'dummy-secret-key'

INSTALLED_APPS = [
    'tests',
]

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, engine='postgres_legacy'),
}

MIDDLEWARE_CLASSES = []
