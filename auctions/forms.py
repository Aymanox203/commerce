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

class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = [
            'amount'
        ]
    
    def __init__(self,*args, **kwargs):
        self.bider = kwargs.pop('bider',None)
        self.listing = kwargs.pop('aListing',None)
        super(BidForm,self).__init__(*args,**kwargs)    
    
    def clean_amount(self,*args,**kwargs):
        data = self.cleaned_data["amount"]
        if data<self.listing.price:
            raise forms.ValidationError("New Bid must be higher than stating price")
        if Bid.objects.filter(listing = self.listing).exists():
            queryset = Bid.objects.filter(listing = self.listing)
            for bid in queryset:
                print(f"amount: {bid.amount}")
                if data <= bid.amount:
                    raise forms.ValidationError("New Bid must be higher than the previous bids")
        return data

            
    


    