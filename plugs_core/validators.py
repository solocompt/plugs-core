from django.utils.translation import ugettext as _
from rest_framework import serializers

class NumberOfDigitsValidator(object):
    """
    Validates if the passed in integer has the
    right number of digits by converting the
    integer to a string and calling len() on it
    """

    message = _('Ensure number of digits is {0}.')

    def __init__(self, digits):
        self.digits = digits

    def __call__(self, value):
        number_of_digits = len(str(value))

        if number_of_digits != self.digits:
            message = self.message.format(self.digits)
            raise serializers.ValidationError(message)

