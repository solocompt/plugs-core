=====
Usage
=====

To use Plugs Core in a project, add it to your `INSTALLED_APPS`:

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
