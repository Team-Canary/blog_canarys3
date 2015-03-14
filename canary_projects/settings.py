# -*- encoding: utf-8 -*-
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


"""
Django settings for canarys_projects project.


##### Dependencias dos projetos ######

# dependencias do app blog

## modulo com suporte a tags, utilizado paar criação do campo de tags no blog
pip install django-taggit

##

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'upmhuq+iyd7out5m!ctz8$v-v4z_enp-4@j*2p-#n0=-d9voa3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Definie quais aplicações do projeto serão ativadas

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'taggit',
    'pagination',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

#define qual o arquivo será o arquivo padrão de configuração dos padroes de url
ROOT_URLCONF = 'canary_projects.urls'

WSGI_APPLICATION = 'canary_projects.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.canary_projects'),
       # 'USER': 'root',
       # 'PASSWORD': '',
       # 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
       # 'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



MEDIA_ROOT= os.path.join(BASE_DIR, "blog/media")
MEDIA_URL='/media/'

STATIC_URL = '/static/'


"""
STATICFILES_DIRS
define o caminho da pasta static,essa pasta é utilizada para armazenar arquivos de
css, js e imagens que compoem o layout
"""

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "blog/static"),
    '/var/www/static/',
)

"""
TEMPLATE_DIRS
essa variavel define o caminho paar a pasta blog, pasta
utilizadas para armazenar os arquivos html do site
"""

#define a fonte de onde os templatesserão carregados
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader', #pasta templates do projeto (/templates)
    'django.template.loaders.app_directories.Loader', #pasta templates do app (/app/templates)
)

#define o caminho das pastas onde seão carregados os templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'blog/templates'),
    os.path.join(BASE_DIR,  'templates'),
)


from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "blog.context_processors.global_vars",
)

