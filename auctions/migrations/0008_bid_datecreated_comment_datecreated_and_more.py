# Generated by Django 4.1 on 2022-11-12 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_bid_listing_listing_watchlist_alter_bid_bider_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='dateCreated',
            field=models.DateField(default=datetime.datetime(2022, 11, 12, 6, 55, 47, 339367)),
        ),
        migrations.AddField(
            model_name='comment',
            name='dateCreated',
            field=models.DateField(default=datetime.datetime(2022, 11, 12, 6, 55, 47, 339367)),
        ),
        migrations.AddField(
            model_name='listing',
            name='dateCreated',
            field=models.DateField(default=datetime.datetime(2022, 11, 12, 6, 55, 47, 338369)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('0', 'All Categories'), ('1', 'Antiques'), ('2', 'Art'), ('3', 'Baby'), ('4', 'Books'), ('5', 'Business & Industrial'), ('6', 'Cameras & Photo'), ('7', 'Cell Phones & Accessories'), ('8', 'Clothing, Shoes & Accessories'), ('9', 'Coins  & Paper Money'), ('10', 'Collectibles'), ('11', 'Computers/Tablets & Networking'), ('12', 'Consumer Electronics'), ('13', 'crafts'), ('14', 'Dolls '), ('15', 'Movies'), ('16', 'Entertainment Memorabilia'), ('17', 'Gift Cards & Coupons'), ('19', 'Health & Beauty'), ('20', 'Home'), ('21', 'Jewelry'), ('22', 'Music'), ('23', 'Musical Instruments'), ('24', 'Gear'), ('25', 'Pet Supplies'), ('26', 'Pottery & Glass'), ('27', 'Real Estate'), ('28', 'Specialty Services'), ('29', 'Sporting Goods'), ('30', 'Sports Mem, Cards'), ('31', 'Tickets & Experiences'), ('32', 'Toys & Hobbies'), ('33', 'Travel'), ('34', 'Vehicles'), ('35', 'Video Games & Consoles'), ('36', 'Everything Else')], default='0', max_length=30, null=True),
        ),
    ]
