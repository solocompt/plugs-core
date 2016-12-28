from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from plugs_core.validators import NumberOfDigitsValidator

class NaiveNIFField(models.PositiveIntegerField):
    """
    Custom model field that represents a portuguese NIF
    this implementation is very naive, it only checks that the
    NIF contains 9 digits
    """

    default_validators = [NumberOfDigitsValidator(9)]

    def __init__(self, *args, **kwargs):
        super(NaiveNIFField, self).__init__(*args, **kwargs)



class PercentageField(models.FloatField):
    """
    Custom model field that represents a percentage in range 0-1
    in order to facilitate calculations with this value
    """
    
    default_validators = [MinValueValidator(0), MaxValueValidator(1)]
    
    def __init__(self, *args, **kwargs):
        super(PercentageField, self).__init__(*args, **kwargs)
