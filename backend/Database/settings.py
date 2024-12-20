import os
from django.core.exceptions import ImproperlyConfigured
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ['DEBUG'])

ALLOWED_HOSTS = ['barrelwisdom.com', 'localhost', '127.0.0.1', 'backend']

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Application definition

DB_TABLES = [

]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'django.contrib.sites',
    'dj_rest_auth',
    # Major parts
    'blog.apps.BlogConfig',
    'invite.apps.InviteConfig',
    'navigation.apps.NavigationConfig',
    'userprofile.apps.UserProfileConfig',
    'report.apps.ReportConfig',
    # A01 Marie
    # A12 Totori
    'games.A12.traits_a12.apps.A12TraitConfig',
    'games.A12.effects_a12.apps.A12EffectConfig',
    'games.A12.categories_a12.apps.A12CategoryConfig',
    'games.A12.regions_a12.apps.A12RegionConfig',
    'games.A12.monsters_a12.apps.A12MonsterConfig',
    'games.A12.items_a12.apps.A12ItemConfig',
    'games.A12.areadata_a12.apps.A12AreaDataConfig',
    # A15 Escha & Logy
    'games.A15.categories_a15.apps.A15CategoryConfig',
    'games.A15.properties_a15.apps.A15PropertyConfig',
    'games.A15.effects_a15.apps.A15EffectConfig',
    'games.A15.regions_a15.apps.A15RegionConfig',
    'games.A15.monsters_a15.apps.A15MonsterConfig',
    'games.A15.items_a15.apps.A15ItemConfig',
    # A16 Shallie
    'games.A16.categories_a16.apps.A16CategoryConfig',
    'games.A16.regions_a16.apps.A16RegionConfig',
    'games.A16.effects_a16.apps.A16EffectConfig',
    'games.A16.properties_a16.apps.A16PropertyConfig',
    'games.A16.monsters_a16.apps.A16MonsterConfig',
    'games.A16.items_a16.apps.A16ItemConfig',
    'games.A16.areadata_a16.apps.A16AreaDataConfig',
    # A18 Firis
    'games.A18.effects_traits_a18.apps.A18EffectTraitConfig',
    'games.A18.misc_a18.apps.A18MiscConfig',
    'games.A18.items_a18.apps.A18ItemConfig',
    'games.A18.monsters_a18.apps.A18MonsterConfig',
    # A21 Ryza 1
    'games.A21.effects_traits_a21.apps.A21EffectTraitConfig',
    # A22 Ryza 2
    'games.A22.effects_a22.apps.A22EffectConfig',
    'games.A22.traits_a22.apps.A22TraitConfig',
    'games.A22.categories_a22.apps.A22CategoryConfig',
    'games.A22.locations_a22.apps.A22LocationConfig',
    'games.A22.items_a22.apps.A22ItemConfig',
    'games.A22.monsters_a22.apps.A22MonsterConfig',
    'games.A22.shops_a22.apps.A22ShopConfig',
    # A23 Sophie 2
    'games.A23.effects_a23.apps.A23EffectConfig',
    'games.A23.traits_a23.apps.A23TraitConfig',
    'games.A23.misc_a23.apps.A23MiscConfig',
    'games.A23.regions_a23.apps.A23RegionConfig',
    'games.A23.items_a23.apps.A23ItemConfig',
    'games.A23.monsters_a23.apps.A23MonsterConfig',
    # A24 Ryza 3
    # A25 Resleri
    'games.A25.misc_a25.apps.A25MiscConfig',
    'games.A25.chara_a25.apps.A25CharaConfig',
    'games.A25.items_a25.apps.A25ItemConfig',
    'games.A25.quest_a25.apps.A25QuestConfig',
    # Blue Reflection
    'games.BR1.missions_br1.apps.BR1MissionConfig',
    'games.BR1.areas_br1.apps.BR1AreaConfig',
    'games.BR1.demons_br1.apps.BR1DemonConfig',
    'games.BR1.skills_br1.apps.BR1SkillConfig',
    'games.BR1.fragments_br1.apps.BR1FragmentConfig',
    'games.BR1.items_br1.apps.BR1ItemConfig',
    # Blue Reflection Second Light
    'games.BRSL.fragments_brsl.apps.BRSLFragmentConfig',
    'games.BRSL.items_brsl.apps.BRSLItemConfig',
    'games.BRSL.facilities_brsl.apps.BRSLFacilityConfig',
    'games.BRSL.skills_brsl.apps.BRSLSkillConfig',
    'games.BRSL.demons_brsl.apps.BRSLDemonConfig',
    'games.BRSL.regions_brsl.apps.BRSLRegionConfig',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    ALLOWED_HOSTS = ['*']
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    # very annoying to have cache on during development
    # but did this ever come back to bite me
    #MIDDLEWARE.remove('django.middleware.cache.UpdateCacheMiddleware')
    #MIDDLEWARE.remove('django.middleware.cache.FetchFromCacheMiddleware')
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'Database.urls'

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

WSGI_APPLICATION = 'Database.wsgi.application'

SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'barrelwisdom',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'postgres',
    },
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':('dj_rest_auth.jwt_auth.JWTCookieAuthentication',),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'] if DEBUG else
        ['rest_framework.renderers.JSONRenderer']
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ALGORITHM': 'RS256',
    'SIGNING_KEY': Path('jwt-key').read_text(),
    'VERIFYING_KEY': Path('jwt-key.pub').read_text(),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'bw-auth'
JWT_AUTH_REFRESH_COOKIE = 'bw-refresh'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    }
}