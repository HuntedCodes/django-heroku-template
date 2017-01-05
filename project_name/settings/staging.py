"""
Staging Django settings for {{ project_name }} project.

Generate SECRET_KEY_STAGING on CLI:
https://gist.github.com/thehappypath/3a86e401db8e0311ba12#file-django-keygen-sh

"""

from .base import *  # noqa

# Security
# Environment variable suffixed with "STAGING" to prevent a mix-up.
SECRET_KEY = os.environ.get('SECRET_KEY_STAGING')

# Tighten up the wildcard host when you have a domain.
ALLOWED_HOSTS = [
    '.herokuapp.com',
]
