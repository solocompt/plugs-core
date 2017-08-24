# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from plugs_core.urls import urlpatterns as plugs_core_urls

urlpatterns = [
    url(r'^', include(plugs_core_urls, namespace='plugs_core')),
]
