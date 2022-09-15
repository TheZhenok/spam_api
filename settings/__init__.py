from django.core.exceptions import ImproperlyConfigured
import os
from dotenv import load_dotenv

from settings.celery import app as celery_app

__all__ = ('celery_app', )


load_dotenv()
def get_env_variable(env_variable: str) -> str:
    try:
        return os.environ[env_variable]
    except KeyError:
        raise ImproperlyConfigured(
            f'Set {env_variable} is false'
        )