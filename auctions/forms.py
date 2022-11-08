from django import forms
from .models import *

class ListingForm(forms.ModelForm):

    class Meta():
        model = Listing
        fields = [
            'title',
            'description',
            'price',
            'image',
            'category'
        ]

        widgets = {
            
        }    

    