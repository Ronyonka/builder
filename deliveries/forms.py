from django import forms

from .models import *

class DeliveryForm(forms.ModelForm):
    '''
    A form that allows users to add businesses
    '''
    class Meta:
        model = Delivery
        fields = ['item', 'quantity', 'date', 'time']