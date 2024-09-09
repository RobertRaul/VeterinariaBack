from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["172.20.10.5"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "sis_zoolomascotas",
        "USER": "sa",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "Trusted_Connection": "yes",
        },
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/" 
