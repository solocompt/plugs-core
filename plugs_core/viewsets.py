"""
Core Viewsets
"""

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin,
    DestroyModelMixin, UpdateModelMixin)


class CreateReadViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides create and read (list and retrieve) actions
    """
    pass

class CreateReadDestroyViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """
    A viewset that provides create, read (list and retrieve) and destroy actions
    """
    pass

class UpdateReadViewSet(UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides update and read (list and retrieve) actions
    """
    pass

class CreateUpdateReadViewSet(CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides create, update and read (list and retrieve) actions
    """
    pass

class CreateViewSet(CreateModelMixin, GenericViewSet):
    """
    A viewset that provides create action
    """
    pass
