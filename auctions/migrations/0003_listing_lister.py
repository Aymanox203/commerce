# Generated by Django 4.1 on 2022-11-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_listing_bider'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='lister',
            field=models.CharField(default='User', max_length=50, unique=True),
        ),
    ]