# settings.py
SECRET_KEY = 'MS3testingSecretKey'
# Use SQLite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database.db',  # BASE_DIR is predefined in Django settings
    }
}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your app
]

DEBUG = False
ALLOWED_HOSTS = ['.herukoapp.com']