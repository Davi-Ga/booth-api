from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class ValidateTest:
    
    def __init__ (self,num):
        self.num = num
    
    def __call__(self,value):
        if not value % 2 == self.num:
            raise ValidationError('Tem que ser par')
        else:
            return value   
    
