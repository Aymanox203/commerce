from locale import currency
from django.core.exceptions import ValidationError

def validateBid(value,currency):
    if value>=1:
        return value
    else: raise ValidationError(f"Bid must be higher Than {currency}1")