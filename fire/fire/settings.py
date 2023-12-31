"""
Django settings for fire project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""



from pathlib import Path
import os
if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n8xki*q+tx6n+f7ui0kl7e+2csu1zto_%seu=@0ow8jw@i()3='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
   
    'location_field.apps.DefaultConfig',

    'map',
    'home',
    'signup',
    'login',
    
    
   
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'FFFP',
        'USER' : 'postgres',
        'PASSWORD': 'mohamed123',
        'HOST' : 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS= [os.path.join(BASE_DIR,'static')]
MEDIA_URL ='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#######################################################################################
# Configurations pour l'envoi d'e-mails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS=True

EMAIL_HOST_USER='demnimohamed88@gmail.com'

EMAIL_HOST_PASSWORD='pwqaowrtzukynkdy'

###################################################################
MQTT_SERVER = 'eu1.cloud.thethings.network'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = 'mohamed-app@ttn'
MQTT_PASSWORD = 'NNSXS.NS6KTDDWGHPESLOJY325VWIASXVKTKA7A6KKZKY.UZIUYALZSUCJHK2H6LL37XSAYKU7BBDNPE7G2KGZQH5CAPNJMPLQ'

# MQTT_SERVER = 'eu1.cloud.thethings.network'
# MQTT_PORT = 1883
# MQTT_KEEPALIVE = 60
# MQTT_USER = 'loraatest02@ttn'
# MQTT_PASSWORD = 'NNSXS.LO6MNFLIDPGXTB4YOKJWMEK2CYCNIODLIVEQ2RY.5THHCR2XZHZXYT4VTZZLNTKNDGLSWCQ2GKFCVW2OID67WKOMI53A'

###########################################################################
LOCATION_FIELD = {
    'provider.openstreetmap.max_zoom': 18,
}

LOCATION_FIELD = {
    'map.provider': 'openstreetmap',
    'search.provider': 'nominatim',
}