
from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

from Crypto.Random import get_random_bytes

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env_path = os.path.join(BASE, '.env')
load_dotenv(dotenv_path=env_path)


SECRET_KEY = os.getenv('SECRET_ACCESS_TOKEN')
DEBUG = os.getenv('DEBUG')

Encryption_key = os.getenv('Encryption_key', get_random_bytes(24))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'Main_app',
    'Community',
    "drf_spectacular",

]

ALLOWED_HOSTS = ['*']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MedikeaAIBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s/Templates/' % (PROJECT_DIR),],
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

WSGI_APPLICATION = 'MedikeaAIBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if os.getenv('ENV') == 'production':
    DATABASES = {
        'default': {
            'ENGINE':os.getenv('ENGINE'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST':os.getenv('HOST'),
            'NAME': os.getenv('NAME'),
            'PORT':os.getenv('PORT')
        }
    }
else:

    DATABASES = {
        'default': {    
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL ='Main_app.User'

# SSO_URL = os.getenv('SSO_URL')
# VISIT_URL = os.getenv('VISIT_URL')
# LABTEST = os.getenv('LABTEST')

SSO_URL='http://localhost:8002'
VISIT_URL='http://127.0.0.1:8000'
LABTEST='http://localhost:8000'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = ('%s/static'%BASE),

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE, 'static/media')

AUTOCOMMIT = True


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10*365),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ['Bearer'],
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ['rest_framework_simplejwt.tokens.AccessToken'],
    'TOKEN_TYPE_CLAIM': 'token_type',
}


CORS_ALLOWED_ORIGINS = [
    'https://*.mmsengine.cloud',
    'https://*.medikea.co.tz',
    'https://medikea.co.tz',
    'https://hospital.medikea.co.tz',
    'http://localhost:4200'
]

CORS_ALLOW_ALL_ORIGINS = False

CSRF_TRUSTED_ORIGINS = [
    'https://*.mmsengine.cloud',
    'https://medikea.co.tz',
    'https://*.medikea.co.tz', 
    'https://hospital.medikea.co.tz',
    'http://localhost:4200' 
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Medical Assistant API',
    'DESCRIPTION': 'Medical Assistant Api Documentation',
    'VERSION': '1.0.0',
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Medical Assistant Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Medical Assistant",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "MAS",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "assets/image/medikea-h-dark.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "assets/image/medikea-h-dark.png",

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": "assets/image/medikea-h-dark.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Medical Assistant system",

    # Copyright on the footer
    "copyright": "Medikea Medical Assistant System",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Medikea Website", "url": "https://medikea.co.tz/home", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generaTrueting side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "Main_app", "books.author", "books.book"],

    # # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "Main_app": [{
            "name":"Setting", 
            "url": "setting_page", 
            "icon": "fas fa-comments",
            "permissions": ["auth.view_user"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Main_app.Occupation": "'fas fa-briefcase'",
        "Main_app.User": "fas fa-user-md",
        "Main_app.DoctorProfile": "fas fa-stethoscope",
        "Main_app.Speciality": "fas fa-user-md",
        "Main_app.Hospital": "fas fa-hospital",
        "Main_app.Symptom": "fas fa-thermometer",
        "Main_app.DiseasePrevention": "fas fa-shield-alt",
        "Main_app.Community": "fas fa-users",
        "Main_app.Drugstore": "fas fa-capsules",
        "Main_app.TeatmentCategory": "fas fa-band-aid",
        "Main_app.Teatment": "fas fa-notes-medical",
        "Main_app.PharmacologicalTreatment": "fas fa-pills",
        "Main_app.Investigations": "fas fa-flask",
        "Main_app.Disease": "fas fa-virus",
        "ModelTrainingResults": "fas fa-file-alt",
        "Main_app.message": "fas fa-envelope",
        "Main_app.Post": 'fas fa-newspaper',
        "Main_app.Comment": 'fas fa-comment-alt',
        "Main_app.Like": "fas fa-thumbs-up",
        "Main_app.Cases": "fas fa-file-medical",
        'Main_app.Resource': "fas fa-file",
        "Main_app.ModelTrainingResults": "fas fa-chart-line",
        "Main_app.DifferentialDiagnosisCategory": "fas fa-list"
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}


REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50

}
