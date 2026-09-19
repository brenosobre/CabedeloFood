"""
Django settings for guia_cidade project.
"""
import os
import dj_database_url
from pathlib import Path

# Constroi os caminhos dentro do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# AVISO DE SEGURANÇA: mantenha a chave secreta protegida em produção!
SECRET_KEY = 'django-insecure-chave-de-teste-local-cabedelofood'

# AVISO DE SEGURANÇA: não rode com DEBUG = True em produção!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Definição dos Aplicativos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurantes',  # <-- Nosso app focado nos restaurantes
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Essencial para arquivos estáticos em produção
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'guia_cidade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'guia_cidade.wsgi.application'


# Banco de dados configurado para ambiente local (SQLite) e compatível com nuvem
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}


# Validação de Senhas
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


# Internacionalização
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Arquivos Estáticos (CSS, JavaScript, Imagens do sistema)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Tipo de campo automático padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- CONFIGURAÇÕES DE UPLOAD DE IMAGENS ---
# URL usada para acessar as imagens no navegador
MEDIA_URL = '/media/'

# Pasta física no seu computador onde as imagens serão salvas
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')