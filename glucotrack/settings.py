
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v(3#-9%a81=spbs1@$ndpzarl@0x$so9+srw*73vanqjh+b@hu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'homepage.CustomUser'
AUTHENTICATION_BACKENDS = [
    'homepage.backends.EmailBackend',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition

INSTALLED_APPS = [

    'widget_tweaks',
    #########################################
    'homepage.apps.HomepageConfig',
    'login.apps.LoginConfig',
    'signup.apps.SignupConfig',

    #########################################Medical staff

    'medical_staff_addblog.apps.MedicalStaffAddblogConfig',
    'medical_staff_blogs.apps.MedicalStaffBlogsConfig',
    'medical_staff_dashboard.apps.MedicalStaffDashboardConfig',
    'medical_staff_patients.apps.MedicalStaffPatientsConfig',
    'medical_prevention_test.apps.MedicalPreventionTestConfig',
    #########################################Patient 
    'patient_blog.apps.PatientBlogConfig',
    'patient_blood.apps.PatientBloodConfig',
    'patient_dashboard.apps.PatientDashboardConfig',
    'patient_fullhistory.apps.PatientFullhistoryConfig',
    'patient_kidsgame.apps.PatientKidsgameConfig',
    'patient_game.apps.PatientGameConfig',
    'patient_mydoctor.apps.PatientMydoctorConfig',
    'patient_prevention_test.apps.PatientPreventionTestConfig',
    'patient_gestational_dashboard.apps.PatientGestationalDashboardConfig',

    ############################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    ############################ remove cash after logout
    'homepage.middlewares.NoCacheMiddleware',
    ############################
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'glucotrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'glucotrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
