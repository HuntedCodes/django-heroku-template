"""
Local Django settings for {{ project_name }} project.

"""

from .base import *  # noqa

# Security
SECRET_KEY = r"{{ secret_key }}"

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# Debugging
DEBUG = True


# Application definition
INSTALLED_APPS += (
    'debug_toolbar',
)
