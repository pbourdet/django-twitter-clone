import os

os.environ["USE_DOT_ENV"] = "YES"

from ._base import *

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"
