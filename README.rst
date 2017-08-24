=============================
Plugs Core
=============================

.. image:: https://badge.fury.io/py/plugs-core.svg
    :target: https://badge.fury.io/py/plugs-core

.. image:: https://travis-ci.org/ricardolobo/plugs-core.svg?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-core

.. image:: https://codecov.io/gh/ricardolobo/plugs-core/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ricardolobo/plugs-core

Your project description goes here

Documentation
-------------

The full documentation is at https://plugs-core.readthedocs.io.

Quickstart
----------

Install Plugs Core::

    pip install plugs-core

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_core.apps.PlugsCoreConfig',
        ...
    )

Add Plugs Core's URL patterns:

.. code-block:: python

    from plugs_core import urls as plugs_core_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_core_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
