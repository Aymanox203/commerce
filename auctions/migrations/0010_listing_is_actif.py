# Generated by Django 4.1 on 2022-11-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_bid_datecreated_alter_comment_datecreated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_actif',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
