from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from .util import validateBid

defaultUsernameField = models.CharField(max_length=50, blank=False, null=False, unique=True)

class User(AbstractUser):
    pass

class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2,
    default=1,
    max_digits=7,
    validators=[validateBid])
    
    bider = defaultUsernameField
    dateCreated = datetime.now()

class Listing(models.Model):
    class Category(models.TextChoices):
            DEFAULT = "0" ,"All Categories"
            ANTIQUE = "1" ,"Antiques"
            ART = "2" ,"Art"
            BABY = "3" ,"Baby"
            BOOKS = "4" ,"Books"
            BUSINESS ="5" ,"Business & Industrial"
            CAMERAS = "6" ,"Cameras & Photo"
            PHONES = "7" ,"Cell Phones & Accessories"
            CLOTHES = "8" ,"Clothing, Shoes & Accessories"
            COINS = "9" ,"Coins  & Paper Money"
            COLLECTIBLES = "10" ,"Collectibles"
            COMPUTERS = "11" ,"Computers/Tablets & Networking"
            ELECTRONICS = "12" ,"Consumer Electronics"
            CRAFTS = "13" ,"crafts"
            DOLLS = "14" ,"Dolls "
            MOVIES = "15" ,"Movies"
            MEMOS = "16" ,"Entertainment Memorabilia"
            GIFTCARDS = "17" ,"Gift Cards & Coupons"
            BEAUTY = "19" ,"Health & Beauty"
            HOME = "20" ,"Home"
            JEWELRY = "21" ,"Jewelry"
            MUSIC = "22" ,"Music"
            INSTRUMENTS = "23" ,"Musical Instruments"
            GEAR = "24" ,"Gear"
            PET_SUP = "25" ,"Pet Supplies"
            POTTERY = "26" ,"Pottery & Glass"
            REAL_ESTATE = "27" ,"Real Estate"
            SERVICES = "28" ,"Specialty Services"
            SPORTS = "29" ,"Sporting Goods"
            CARDS = "30" ,"Sports Mem, Cards"
            TICKETS = "31" ,"Tickets & Experiences"
            TOYS = "32" ,"Toys & Hobbies"
            TRAVEL = "33" ,"Travel"
            GAMES_CONSOLES = "34" ,"Video Games & Consoles"
            ELSE = "35" ,"Everything Else"
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, default=0, max_digits=7)
    image = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.DEFAULT,null=True, blank=True)
    dateCreated = datetime.now()
    bids = []
    lister = defaultUsernameField

class Comment(models.Model):
    commenter = defaultUsernameField
    content = models.TextField()
    dateCreated = datetime.now()