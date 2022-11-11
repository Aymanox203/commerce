from locale import currency
from django.core.exceptions import ValidationError
from .models import Bid

def validateBid(value,currency):
    if value<=1:
        return value
    else: raise ValidationError(f"Bid must be higher Than {currency}1")



