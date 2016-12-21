"""
Custom Serializers Classes
"""

from rest_framework import serializers


class PrivateFieldsModelSerializer(serializers.ModelSerializer):
    """
    Subclasses ModelSerialzer to add the ability to restrict some
    fields when marked as private

    private_fields must be a tuple or list

    ...
    private_fields = ('email', )

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            kwargs['private_fields'] = self.private_fields
        return super(UserViewSet, self).get_serializer(*args, **kwargs)
    """
    def __init__(self, *args, **kwargs):
        """
        Dealing with private fields
        """
        private = kwargs.pop('private_fields', None)
        super(PrivateFieldsModelSerializer, self).__init__(*args, **kwargs)
        if private is not None:
            for field_name in private:
                self.fields.pop(field_name)
