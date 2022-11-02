from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from .util import validateBid

defaultUsernameField = models.CharField(max_length=50, blank=False, null=False, unique=True)

class User(AbstractUser):
    username = defaultUsernameField
    email = models.EmailField( unique=True)
    bids = []
    REQUIRED_FIELDS = ['email']
    def __str__(self):
      return "{}".format(self.email)
    

class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2,
    default=1,
    max_digits=7,
    validators=[validateBid])
    
    bider = defaultUsernameField
    dateCreated = datetime.now()

class Listing(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, default=0, max_digits=7)
    bids = []
    dateCreated = datetime.now()
    lister = defaultUsernameField

class Comment(models.Model):
    commenter = defaultUsernameField
    content = models.TextField()
    dateCreated = datetime.now()
    





