from django import forms

from .models import Details

class ProductForm(forms.ModelForm):
    class Meta:
        model = Details
        field  = [
            'year', 
            'name',
            'price',
            'stockNumber'
        ]
        exclude = ()