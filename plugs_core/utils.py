"""
Temp Utils Module
"""

import re
import string
import random
import logging

from django.conf import settings
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

LOGGER = logging.getLogger(__name__)


def camel_to_snake(name):
    """
    Convert from CamelCase to snake_case
    http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_db_distinct(queryset, field, func, **params):
    """
    Checks if a field / value pair exists in database
    and continues generating values until it finds
    a one that does not exist

    func is the function that generates values and
    params is the parameters that function takes
    """
    while True:
        try:
            value = func(**params)
            queryset.get(**{field: value})
        except ObjectDoesNotExist:
            break
    return value


def get_model_class(name):
    """
    This is being implemented to help
    with the Email Module, where we
    want to use a model for the email
    context without needing to import
    the model (which is most cases create
    a circular dependency, anyway)

    Beware that currently implementation
    returns the first match, so if a model
    with a same name exists in two different
    applications this will not work

    http://stackoverflow.com/a/13242421
    """
    LOGGER.warning('Beware, function returns first match in the model registry.')
    # iterate all registered models
    for model in apps.get_models():
        # return the app_label for first match
        if name == model._meta.object_name:
            app_label = model._meta.app_label
    return apps.get_model(app_label, name)


def get_non_field_errors_key():
    """
    Non field errors key can be override
    in the settings file, but is has a default value
    """
    try:
        key = settings.NON_FIELD_ERRORS_KEY
    except AttributeError:
        key = 'non_field_errors'
    return key


def random_string(**kwargs):
    """
    By default generates a random string of 10 chars composed
    of digits and ascii lowercase letters. String length and pool can
    be override by using kwargs. Pool must be a list of strings
    """
    n = kwargs.get('length', 10)
    pool = kwargs.get('pool') or string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(pool) for _ in range(n))
