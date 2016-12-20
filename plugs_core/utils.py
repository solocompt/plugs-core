"""
Temp Utils Module
"""

import re
import string
import random
import logging
from lxml import html

from django.conf import settings
from django.apps import apps
from django.contrib.auth import get_user_model
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


def html_to_text(html_string):
    """
    returns a plain text string when given a html string text
    handles a, p, h1 to h6 and br, inserts newline chars to
    create space in the string
    @todo handle images
    """
    # create a valid html document from string
    # beware that it inserts <hmtl> <body> and <p> tags
    # where needed
    html_tree = html.document_fromstring(html_string)

    # handle header tags
    for h in html_tree.cssselect("h1, h2, h3, h4, h5, h6"):
        # add two newlines after a header tag
        h.text = h.text + '\n\n'
        
    # handle links
    # find all a tags starting from the root of the document //
    # and replace the link with (link)
    for a in html_tree.xpath("//a"):
        href = a.attrib['href']
        a.text = a.text + " (" + href + ")"

    # handle paragraphs
    for p in html_tree.xpath("//p"):
        # keep the tail if there is one
        # or add two newlines after the text if there is no tail
        p.tail = p.tail if p.tail else "\n\n"

    # handle breaks
    for br in html_tree.xpath("//br"):
        # add a newline and then the tail (remaining text after the <br/> tag)
        # or add a newline only if there is no tail
        # http://stackoverflow.com/questions/18660382/how-can-i-preserve-br-as-newlines-with-lxml-html-text-content-or-equivalent?rq=1
        br.tail = "\n" + br.tail if br.tail else "\n"
        
    return html_tree.text_content()


def random_string(**kwargs):
    """
    By default generates a random string of 10 chars composed
    of digits and ascii lowercase letters. String length and pool can
    be override by using kwargs. Pool must be a list of strings
    """
    n = kwargs.get('length', 10)
    pool = kwargs.get('pool') or string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(pool) for _ in range(n))
