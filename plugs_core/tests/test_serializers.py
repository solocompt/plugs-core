"""
Testing Serializers
"""

from django.db import models
from django.test import SimpleTestCase

from plugs_core.serializers import PrivateFieldsModelSerializer


class TestModel(models.Model):
    public_field = models.CharField(max_length=100)
    private_field = models.CharField(max_length=100)


class TestSerializer(PrivateFieldsModelSerializer):
    class Meta:
        model = TestModel
        fields = ('public_field', 'private_field')


class TestViews(SimpleTestCase):
    """
    Testing Serializers
    """


    def test_private_fields_model_serializer_with_empty_tuple(self):
        """
        Ensures empty private fields tuple does not affect serializer
        """
        private_fields = ()
        data = { 'public_field': 'foo', 'private_field': 'bar' }
        kwargs = { 'private_fields': private_fields }
        serializer = TestSerializer(data=data, **kwargs)
        serializer.is_valid()
        self.assertEqual(data, serializer.data)


    def test_private_fields_model_serializer(self):
        """
        Ensures private fields are not present in serializer data
        """
        private_fields = ('private_field', )
        data = { 'public_field': 'foo', 'private_field': 'bar' }
        kwargs = { 'private_fields': private_fields }
        serializer = TestSerializer(data=data, **kwargs)
        serializer.is_valid()
        data.pop('private_field')
        self.assertEqual(data, serializer.data)
